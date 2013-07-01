from django.db import models

# Create your models here.

class Users(models.Model):
	first name = models.CharField(max_length=15)
	last name = models.CharField(max_length=20)
	email address = models.CharField(max_length=32)
	


