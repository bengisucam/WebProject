from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import SignupForm
from .models import User
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import logout


def signupPage(request):
    if request.method == 'POST':
        signupForm = SignupForm(request.POST)
        if signupForm.is_valid():
            email = signupForm.cleaned_data.get('email')
            user_list = User.objects.all()
            if not user_list.filter(email=email).exists():
                signup = signupForm.save(commit=False)
                signup.password = make_password(signupForm.cleaned_data.get('password'))
                signup.save()
            else:
                messages.error(request, 'User already exists!')
                return redirect('signupForm')
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
            if check_password(password, user.password):
                pk = user.pk
                # return redirect('homeForm', pk=pk)
                return HttpResponseRedirect(reverse('homeForm', args=(pk,)))
            else:
                messages.error(request, 'Password is not correct!')
        except Exception as e:
            print(e)
            messages.error(request, 'Email does not exists!')
            return render(request, 'accounts/login.html')
    context = {}
    return render(request, 'accounts/login.html', context)




def logoutPage(request, user_id):
    logout(request)
    return redirect('loginForm')



def home(request, user_id):
    active_user = User.objects.get(pk=user_id)
    return render(request, 'accounts/base_login.html', {'active_user': active_user})
