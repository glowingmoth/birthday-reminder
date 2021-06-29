from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def register(request):
  context = {}
  return render(request, 'users/register.html', context)

def login(request):
  context = {}
  return render(request, 'users/login.html', context)
