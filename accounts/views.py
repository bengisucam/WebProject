from django.shortcuts import render

# Create your views here.

def cerate_account(request):
    return render(request, 'accounts/login.html');