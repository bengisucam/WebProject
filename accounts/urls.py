from django.urls import path
from . import views

# seperate each app url individual files, dont overwhelm the WebProject/urls.py !

urlpatterns = [
    path('login/', views.loginPage, name='loginForm'),
    path('signup/', views.signupPage, name='signupForm'),
    path('login/<int:user_id>/home/', views.home, name='homeForm')

]
