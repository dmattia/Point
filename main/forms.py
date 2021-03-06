from django import forms
from userprofile.models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from material import Layout, Row

class PlayerCreationForm(UserCreationForm):
	email = forms.EmailField(required=True)
	position = forms.ChoiceField(choices=UserProfile.POSITION_CHOICES)
	foot = forms.ChoiceField(choices=UserProfile.FOOT_CHOICES)

	class Meta:
		model = UserProfile
		fields = ('username', 'first_name', 'last_name', 'age', 'position', 'height', 'foot')

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
	min_age = forms.IntegerField()
	max_age = forms.IntegerField()
	min_height = forms.IntegerField()
	max_height = forms.IntegerField()

	layout = Layout(
		Row('min_age', 'max_age'),
		Row('min_height', 'max_height'),
		'foot', 'position'
	)

	class Meta:
		model = UserProfile
		fields = ('foot', 'position',)
