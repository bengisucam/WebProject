from django.urls import path
from . import views

# seperate each app url individual files, dont overwhelm the WebProject/urls.py !

urlpatterns = [
    path('', views.list_news),
    path('create/', views.create_news)
]