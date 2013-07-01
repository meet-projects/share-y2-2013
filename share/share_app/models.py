from django.db import models

# Create your models here.

class Users(models.Model):
	firstname = models.CharField(max_length=15)
	lastname = models.CharField(max_length=20)
	emailaddress = models.CharField(max_length=32)
	


