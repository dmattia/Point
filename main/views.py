from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from forms import PlayerCreationForm, LogInForm, PlayerSearchForm
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.urlresolvers import reverse
from userprofile.models import UserProfile, SkillUpvote

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
	args = {
		'loginForm': LogInForm()
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
	args = {
		'user': user,
		'skills': skills,
	}
	return render(request, 'profile.html', args)
