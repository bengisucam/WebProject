from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import SignupForm
from .models import User


def signupPage(request):
    if request.method == 'POST':
        signupForm = SignupForm(request.POST)
        if signupForm.is_valid():
            email = signupForm.cleaned_data.get('email')
            user_list = User.objects.all()
            if not user_list.filter(email=email).exists():
                signupForm.save()
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
            if user.password == password:
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




def home(request, user_id):
    active_user = User.objects.get(pk=user_id)
    return render(request, 'accounts/base_login.html', {'active_user': active_user})
