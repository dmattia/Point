from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from forms import PlayerCreationForm, LogInForm, PlayerSearchForm
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.urlresolvers import reverse
from userprofile.models import UserProfile, SkillUpvote
from random import randint
from django import forms

@login_required
def home(request):
	"""
	The homepage for a logged in user
	Input: @request: standard django request object
	Returns: A form to search for players
	"""
	params = {
		'form': PlayerSearchForm(),
	}
	return render(request, 'home.html', params)

def searchResult(request):
	"""
	Search Results for the  main player search page
	Input: @request: standard django request object
	Returns: A list of players matching the search parameters
	Important Local Vars:
		@match: UserProfile objects matching the search criteria
	"""
	if request.method == 'POST':
		form = PlayerSearchForm(request.POST)
		min_age = request.POST['min_age'] if request.POST['min_age'] else 1
		max_age = request.POST['max_age'] if request.POST['max_age'] else 300
		min_height = request.POST['min_height'] if request.POST['min_height'] else 1
		max_height = request.POST['max_height'] if request.POST['max_height'] else 300

		match = UserProfile.objects.all().filter(age__gte=int(min_age)).filter(age__lte=int(max_age)).filter(height__gte=int(min_height)).filter(height__lte=int(max_height))
		args = {
			'results': match,
		}
	else:
		args = {
			'results': UserProfile.objects.all()
		}
	return render(request, 'searchResult.html', args)


def login(request):	
	"""
	Attempts to log in a user on a POST request,
	simply displays a log in form otherwise
	Input: @request: standard django request object
	Output:
		1) Homepage if user logs in correctly
		2) Log in page again if incorrect attempt or first time viewing
	"""
	if request.method == 'POST':
		form = LogInForm(request.POST)
		username = request.POST['username']	
		password = request.POST['password']	
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			# TODO: Go to the next parameter of the url instead of
			# always goint to the home page
			return HttpResponseRedirect(reverse('home'))
		else:
			args = {
				'message': 'Could not find this username/password pair',
				'loginForm': LogInForm(),
			}
			return render(request, 'login.html', args)
	form = LogInForm()
	form.fields['password'].widget = forms.PasswordInput()
	args = {
		'loginForm': form
	}
	return render(request, 'login.html', args)

def logout(request):
	"""
	Logs out a user and returns them to the login screen
	"""
	auth.logout(request)
	return HttpResponseRedirect(reverse('login'))

def register(request):
	"""
	Displays an empty registration form first time.
	Processes a registration request on a POST request
	"""
	if request.method == 'POST':
		form = PlayerCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('home'))
		else:
			args = {
				'registerForm': form
			}
			return render(request, 'register.html', args)
	else:
		args = {
			'registerForm': PlayerCreationForm()
		}
		return render(request, 'register.html', args)

def profile(request, profile_id):
	"""
	Displays a user profile for the user that has id @profile_id
	Input: @profile_id: The id for a UserProfile
	Output: A page displaying information about this UserProfile
	"""
	user = UserProfile.objects.get(id=profile_id)
	skills = [skill[1] for skill in SkillUpvote.SKILL_CHOICES]

	#skill_counts is temporary to fake skill upvotes
	skill_counts = []
	for skill in skills:
		count = range(randint(1,8))	
		padding = 9 - len(count)
		skill_counts.append((skill, count, padding))

	args = {
		'user': user,
		'skill_counts': skill_counts,
	}
	return render(request, 'profile.html', args)
