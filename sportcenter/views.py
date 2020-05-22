from django.shortcuts import render


# Create your views here.
def sport_center_list(request):
    return render(request, 'sportcenter/sport_center_list.html')
