from django.urls import path
from . import views

# seperate each app url individual files, dont overwhelm the WebProject/urls.py !

urlpatterns = [
    path('news/', views.list_news, name='list_news'),
    path('news/create/', views.create_news, name='create_news'),
    path('news/delete/<int:news_id>', views.delete_new, name='delete_news'),
    path('news/details/<int:news_id>', views.details_new, name='details_news')
    #path('news/update/<int:news_id>', views.update_new, name='update_news')
]
