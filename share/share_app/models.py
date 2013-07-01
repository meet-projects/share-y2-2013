from django.db import models
from django.contrib.auth import authenticate

# Create your models here.

class Users(models.Model):
	firstname = models.CharField(max_length=15)
	lastname = models.CharField(max_length=20)
	emailaddress = models.CharField(max_length=32)


	


