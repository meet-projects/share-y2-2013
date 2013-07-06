# Create your views here.
from django.shortcuts import render
from models import Profile, Info
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
def home(request):
  happies = Info.objects.filter(mood="Happy")
  saddies = Info.objects.filter(mood="Sad")
  angries = Info.objects.filter(mood="Angry")
  annoyies = Info.objects.filter(mood="Annoyed")
  sleepies = Info.objects.filter(mood="Sleepy")
  happies_num = len(happies)
  saddies_num = len(saddies)
  angries_num = len(angries)
  annoyies_num = len(annoyies)
  sleepies_num = len(sleepies)
  context = { 'happies':happies_num,'saddies':saddies_num,'angries':angries_num,'annoyies':annoyies_num,'sleepies':sleepies_num}
  return render(request, 'share_app/Homepage.html', context)

def profile(request):
  user = request.user
  profile = Profile.objects.filter(user = user)
  print profile
  happies = Info.objects.filter(mood="Happy", profile=profile[0])
  saddies = Info.objects.filter(mood="Sad", profile=profile[0])
  angries = Info.objects.filter(mood="Angry", profile=profile[0])
  annoyies = Info.objects.filter(mood="Annoyed", profile=profile[0])
  sleepies = Info.objects.filter(mood="Sleepy", profile=profile[0])
  happies_num = len(happies)
  saddies_num = len(saddies)
  angries_num = len(angries)
  annoyies_num = len(annoyies)
  sleepies_num = len(sleepies)
  context = {'user':profile[0], 'happies':happies_num,'saddies':saddies_num,'angries':angries_num,'annoyies':annoyies_num,'sleepies':sleepies_num}
  return render(request, 'share_app/profile.html', context)

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
			return HttpRespose("INVALID USER ASS")
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
	moodinfo = Info.objects.create (mood = request.POST['mood'], profile=profile)
	moodinfo.save()
	return HttpResponseRedirect('profile')

