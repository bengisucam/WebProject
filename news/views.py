from datetime import datetime

from django.shortcuts import render
from .models import News
from accounts.models import User


# Create your views here.


def list_news(request):
    news = News.objects.select_related('instructor_id').order_by('-date')
    return render(request, 'news/list_news.html', {'news': news})


def create_news(request):
    title = request.POST.get("title")
    desc = request.POST.get("desc")
    instructor = User.objects.get(pk=3)
    news = News(title=title, date=datetime.now(), description=desc, likes=0, instructor_id=instructor)
    news.save()
    return list_news(request)


def delete_new(request, news_id):
    news = News.objects.get(pk=news_id)
    news.delete()
    return list_news(request)


def details_new(request, news_id):
    news = News.objects.get(pk=news_id)
    return render(request, 'news/details_new.html', {'detail_new': news})
