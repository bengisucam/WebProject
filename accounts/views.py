from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from . import forms
from accounts.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import SignupForm
from .models import User


# Create your views here.


def signupPage(request):
    if request.method == 'POST':
        signupForm = SignupForm(request.POST)
        if signupForm.is_valid():
            print('saving user')
            signupForm.save()
            # log the user in
            return redirect('loginForm')
    else:
        signupForm = SignupForm()
    return render(request, 'accounts/signup.html', {'signupForm': signupForm})


def loginPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
            if user.password == password:
                pk = user.pk
                return redirect('news', pk=pk)
            else:
                messages.error(request, 'Password is not correct!')
        except:
            messages.error(request, 'Email does not exists!')
            return render(request, 'accounts/login.html')
    context = {}
    return render(request, 'accounts/login.html', context)




def home(request, user_id):
    user_id = 3
    active_user = User.objects.get(pk=3)
    return render(request, 'accounts/base_login.html', {'active_user': active_user})
