from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def homepage(request):
    # very simple response
    # return HttpResponse("HOMEPAGE");

    # render a view
    return render(request, 'homepage.html');