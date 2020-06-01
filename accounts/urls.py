from django.urls import path
from . import views
from news.views import list_news, create_news

# seperate each app url individual files, dont overwhelm the WebProject/urls.py !

urlpatterns = [
    path('login/', views.loginPage, name='loginForm'),
    path('signup/', views.signupPage, name='signupForm'),
    path('login/<int:pk>/news/', list_news, name='news'),
]