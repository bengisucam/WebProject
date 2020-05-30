from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignupForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend




# Create your views here.


def signupPage(request):

    if request.method == 'POST':
        signupForm = SignupForm(request.POST)
        if signupForm.is_valid():
            signupForm.save()
            # log the user in
            return redirect('news:list')
    else:
        signupForm = SignupForm()
    return render(request, 'accounts/signup.html', {'signupForm':signupForm})



def loginPage(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email)
        print(password)
        user = authenticate(username=email, password=password)
        if user is not None:
            print("here in loginPage")
            login(request, user)
            return redirect('news:list')
    context = {}
    return render(request, 'accounts/login.html', context)



#
# def login(request):
#
#     if request.method == 'POST':
#         loginForm = AuthenticationForm()
#     else:
#         loginForm = AuthenticationForm()
#     return render(request, 'accounts/login.html', {'loginForm':loginForm})

