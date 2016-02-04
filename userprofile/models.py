from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class UserProfile(User):
	"""
	An extension of the default User class provided by Django
	Additional Fields:
		@user: the user this model extends
		@age: Age of a player in years
		@height: The height of a player in centimeters
		@foot: A players strong foot
		@position: A players position

	TODO: Add more position options, leagues, teams, and nationalities
	"""
	user = models.OneToOneField(User)
	age = models.IntegerField()
	height = models.IntegerField()
	# Foot enum
	RIGHT = 'R'
	LEFT = 'L'
	BOTH = 'B'
	FOOT_CHOICES = (
		(RIGHT, 'Right'),
		(LEFT, 'Left'),
		(BOTH, 'Both'),
	)
	foot = models.CharField(max_length=1, choices=FOOT_CHOICES, default=RIGHT)
	# Position enum
	FORWARD = 'F'
	MIDFIELDER = 'M'
	DEFENSEMAN = 'D'
	GOALIE = 'G'
	POSITION_CHOICES = (
		(FORWARD, 'Forward'),
		(MIDFIELDER, 'Midfielder'),
		(DEFENSEMAN, 'Defenseman'),
		(GOALIE, 'Goalie'),
	)
	position = models.CharField(max_length=1, choices=POSITION_CHOICES, default=FORWARD)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

admin.site.register(UserProfile)
