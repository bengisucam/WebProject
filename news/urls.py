from django.urls import path
from . import views

# seperate each app url individual files, dont overwhelm the WebProject/urls.py !

app_name = 'news'

urlpatterns = [
    path('', views.list_news, name="list"),
    path('create/', views.create_news, name="create")
]