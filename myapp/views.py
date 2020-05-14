from django.shortcuts import render

# Create your views here.


def myapp_list(request):
    return render(request, 'myapp/myapp_list.html');