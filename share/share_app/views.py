# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate

def home(request):
  return render(request, 'share_app/Homepage.html', {})

def profile(request):
  return render(request, 'share_app/profile.html', {})

def login(request):
  return render(request, 'share_app/login.html', {})

def submitlogin(request):
	UserName = request.POST['username']
	Password = request.POST['password']
	user= authenticate(username=UserName, password=Password)
	if user is not None:
		if user.is_active:
			login(request, user)
		else:
			print "nonono"
	else:
		print "INVALID !!!!!!!!!!!!!!"
	return HttpResponseRedirect('home')

def signup(request):
	print "I am going to work"
	User.objects.create_user(username=request.POST['username2'], email=request.POST["email"],password=request.POST["password2"],first_name=request.POST["firstname"], last_name=request.POST["lastname"])
	 
	
