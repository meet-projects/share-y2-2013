from django.db import models
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
	hobbies = models.CharField(max_length=200)
	school = models.CharField(max_length=50)
	birthday = models.DateField()
	username = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	user = models.OneToOneField(User)

	

	


