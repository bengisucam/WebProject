from django.shortcuts import render
from .models import News

# Create your views here.


def list_news(request):
    news = News.objects.all().order_by('date')
    return render(request, 'news/list_news.html', {'news': news})


def create_news(request):
    return render(request, 'news/create_news.html')