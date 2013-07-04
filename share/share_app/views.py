# Create your views here.
from django.shortcuts import render
from models import Profile
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
def home(request):
  return render(request, 'share_app/Homepage.html', {})

def profile(request):
  user = request.user
  profile = Profile.objects.filter(user = user)
  print profile[0].hobbies
  return render(request, 'share_app/profile.html', {'user':profile[0]})

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
			return HttpRespose("INVALID USER")
	else:
		return HttpResponse("INVALID USER!")
	return HttpResponseRedirect('home')

def signup(request):
	user1 = User.objects.create_user(username=request.POST['username'], email=request.POST["email"],password=request.POST["password"],first_name=request.POST["first_name"], last_name=request.POST["last_name"])
	
	birthdate = datetime.datetime(int(request.POST['birthday_year']), int(request.POST['birthday_month']), int(request.POST['birthday_day']))
	profile = Profile.objects.create(hobbies = request.POST['hobbies'],school = request.POST['school'], birthday = birthdate, user = user1)
	profile.save()
	user = authenticate(username=request.POST['username'], password=request.POST['password'])
	login(request, user)
	return HttpResponseRedirect('home')

def logout_user(request):
	logout(request)
	return HttpResponseRedirect('login')

def mood(request):
	user = request.user
	profile = Profile.objects.filter(user = user)[0]
	moodinfo = Info.objects.create (mood = request.POST['moood'], profile=profile)
	moodinfo.save()
	return HttpResponse('profile')

