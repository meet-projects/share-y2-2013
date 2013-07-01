# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect

def home(request):
  return render(request, 'share_app/Homepage.html', {})

def profile(request):
  return render(request, 'share_app/profile.html', {})

def login(request):
  return render(request, 'share_app/login.html', {})

def submitlogin(request):
  UserName = request.POST['username']
  Password = request.POST['password']
  return HttpResponseRedirect('home')
