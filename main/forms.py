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
		if commit:
			user.save()
		return user
