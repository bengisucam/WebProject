from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from . import forms
from accounts.models import User


# Create your views here.


def signup(request):
    signupForm = UserCreationForm()
    return render(request, 'accounts/signup.html', {'signupForm': signupForm})


def login(request):
    loginForm = forms.login
    return render(request, 'accounts/login.html', {'loginForm': loginForm})


def home(request, user_id):
    user_id = 3
    active_user = User.objects.get(pk=3)
    return render(request, 'accounts/base_login.html', {'active_user': active_user})
