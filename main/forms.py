from django import forms
from userprofile.models import UserProfile
from django.contrib.auth.forms import UserCreationForm

class PlayerCreationForm(UserCreationForm):
	email = forms.EmailField(required=True)
	position = forms.ChoiceField(choices=UserProfile.POSITION_CHOICES)
	foot = forms.ChoiceField(choices=UserProfile.FOOT_CHOICES)

	class Meta:
		model = UserProfile
		fields = ('username', 'age', 'position', 'height', 'foot')

	def save(self, commit=True):
		user = super(PlayerCreationForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.position = self.cleaned_data['position']
		user.foot = self.cleaned_data['foot']
		if commit:
			user.save()
		return user

class LogInForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('username', 'password')

class PlayerSearchForm(forms.ModelForm):
	#position = forms.ChoiceField(choices=UserProfile.POSITION_CHOICES)
	#foot = forms.ChoiceField(choices=UserProfile.FOOT_CHOICES)

	class Meta:
		model = UserProfile
		fields = ('age', 'height', 'foot', 'position',)
