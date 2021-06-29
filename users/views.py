from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from .forms import CreateUserForm

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'users/register.html', context)

def login(request):
    if request.meth == 'POST':
        request.POST.get('username')
        request.POST.get('password')

    context = {}
    return render(request, 'users/login.html', context)
