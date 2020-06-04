from datetime import datetime

from django.contrib import messages
from django.shortcuts import render
from .models import News
from accounts.models import User


# Create your views here.


def list_news(request, user_id):
    active_user = User.objects.get(pk=user_id)
    news = News.objects.select_related('instructor_id').order_by('-date')
    return render(request, 'news/list_news.html', {'news': news, 'active_user': active_user})


def add_news(request, user_id):
    active_user = User.objects.get(pk=user_id)
    return render(request, 'news/add_new.html', {'active_user': active_user})


def create_news(request, user_id):
    active_user = User.objects.get(pk=user_id)
    title = request.POST.get("title")
    desc = request.POST.get("desc")
    if len(title)>0 and len(desc)>0:
        new_news = News(title=title, date=datetime.now(), description=desc, likes=0, instructor_id=active_user)
        new_news.save()
        news_obj = News.objects.select_related('instructor_id').order_by('-date')
    else:
        messages.error(request, 'Please fill all the blanks!')
        return render(request, 'news/add_new.html',
                              {'active_user': active_user})
    return render(request, 'news/list_news.html', {'active_user': active_user, 'news': news_obj})


def delete_new(request, user_id, news_id):
    deleted_news = News.objects.get(pk=news_id)
    deleted_news.delete()
    return list_news(request, user_id)


def details_new(request, user_id, news_id):
    news = News.objects.get(pk=news_id)
    active_user = User.objects.get(pk=user_id)
    return render(request, 'news/details_new.html', {'active_user': active_user, 'detail_new': news})
