from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def signup(request):
    signupForm = UserCreationForm()
    return render(request, 'accounts/signup.html', {'signupForm':signupForm})


def login(request):
    return render(request, 'accounts/login.html')

