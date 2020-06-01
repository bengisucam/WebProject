from django.shortcuts import render
from .models import News

# Create your views here.


def list_news(request, pk):
    news = News.objects.all().order_by('date')
    return render(request.__format__(pk), 'news/list_news.html', {'news': news})


def create_news(request):
    return render(request, 'news/create_news.html')