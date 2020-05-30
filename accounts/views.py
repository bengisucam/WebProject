from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from . import forms


# Create your views here.


def signup(request):
    signupForm = UserCreationForm()
    return render(request, 'accounts/signup.html', {'signupForm': signupForm})


def login(request):
    loginForm = forms.login
    return render(request, 'accounts/login.html', {'loginForm': loginForm})


def home(request):
    return render(request, 'accounts/base_login.html')


