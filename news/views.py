from django.shortcuts import render


# Create your views here.


def list_news(request):
    return render(request, 'news/news.html')
