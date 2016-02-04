from django.shortcuts import render

# Create your views here.
def home(request):
	params = {
		'message': 'hello',
	}
	return render(request, 'home.html', params)
