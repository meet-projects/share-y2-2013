# Create your views here.
from django.shortcuts import render

def home(request):
  return render(request, 'share_app/Homepage.html', {})

def profile(request):
  return render(request, 'share_app/profile.html', {})

def login(request):
  return render(request, 'share_app/login.html', {})

