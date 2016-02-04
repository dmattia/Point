from django.shortcuts import render
from forms import PlayerCreationForm
from django.http import HttpResponseRedirect

def home(request):
	params = {
		'message': 'hello',
	}
	return render(request, 'home.html', params)

def login(request):
	return render(request, 'login.html')

def register(request):
	if request.method == 'POST':
		form = PlayerCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
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
