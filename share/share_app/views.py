# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
def home(request):
  return render(request, 'share_app/Homepage.html', {})

def profile(request):
  return render(request, 'share_app/profile.html', {})

def login_user(request):
  return render(request, 'share_app/login.html', {})

def submitlogin(request):
	user1 = request.POST.get('username',False)
	pwd = request.POST.get('password',False)
	user= authenticate(username=user1, password=pwd)
	if user is not None:
		if user.is_active:
			login(request, user)
		else:
			return HttpRespose("nonono")
	else:
		return HttpResponse("INVALID !!!!!!!!!!!!!!")
	return HttpResponseRedirect('home')

def signup(request):
	User.objects.create_user(username=request.POST['username'], email=request.POST["email"],password=request.POST["password"],first_name=request.POST["firstname"], last_name=request.POST["lastname"])
	user = authenticate(username=request.POST['username'],
                            password=request.POST['password'])
	login(request, user)
	return HttpResponseRedirect('home')

def logout_user(request):
	logout(request)
	return HttpResponseRedirect('login')
