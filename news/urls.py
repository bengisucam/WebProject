from django.urls import path
from . import views

# seperate each app url individual files, dont overwhelm the WebProject/urls.py !

urlpatterns = [
    path('<int:user_id>/news/', views.list_news, name='list_news'),
    path('<int:user_id>/news/add/', views.add_news, name='add_news'),
    path('<int:user_id>/news/create/', views.create_news, name='create_news'),
    path('<int:user_id>/news/delete/<int:news_id>/', views.delete_new, name='delete_news'),
    path('<int:user_id>/news/details/<int:news_id>/', views.details_new, name='details_news'),
    path('<int:user_id>/news/update/<int:news_id>/', views.update_new, name='update_news'),
    path('<int:user_id>/news/update/action/<int:news_id>/', views.update_new_action, name='update_news_action')
]
