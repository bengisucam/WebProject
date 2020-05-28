from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm, LoginForm

# Create your views here.


def signup(request):

    if request.method == 'POST':
        signupForm = SignupForm(request.POST)
        if signupForm.is_valid():
            signupForm.save()
            # log the user in
            return redirect('news:list')
    else:
        signupForm = SignupForm()
    return render(request, 'accounts/signup.html', {'signupForm':signupForm})





def login(request):

    loginForm = LoginForm()
    return render(request, 'accounts/login.html', {'loginForm':loginForm})

