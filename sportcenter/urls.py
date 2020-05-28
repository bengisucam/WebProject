from django.urls import path
from . import views

# seperate each app url individual files, dont overwhelm the WebProject/urls.py !

urlpatterns = [
    path('list/', views.sport_center_list),
]