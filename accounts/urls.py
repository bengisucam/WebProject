from django.urls import path
from . import views

# seperate each app url individual files, dont overwhelm the WebProject/urls.py !

urlpatterns = [
    path('login/', views.login, name='loginForm'),
    path('signup/', views.signup, name='signupForm'),
    path('login/home/', views.home, name='homeForm')

]
