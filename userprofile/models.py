from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class UserProfile(User):
	user = models.OneToOneField(User)
	age = models.IntegerField()
	height = models.IntegerField()
	# Foot enum
	RIGHT = 'R'
	LEFT = 'L'
	FOOT_CHOICES = (
		(RIGHT, 'Right'),
		(LEFT, 'Left'),
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
