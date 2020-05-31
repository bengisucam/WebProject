from django.urls import path
from . import views

# seperate each app url individual files, dont overwhelm the WebProject/urls.py !

urlpatterns = [
    path('<int:user_id>/rooms/', views.list_myrooms, name='list_myrooms'),
    path('<int:user_id>/rooms/add/', views.add_room, name='add_room'),
    path('<int:user_id>/rooms/create/', views.create_room, name='create_room'),
    path('<int:user_id>/rooms/delete/<int:room_id>/', views.delete_room, name='delete_room'),
    path('<int:user_id>/rooms/update/<int:room_id>/', views.update_room, name='update_room'),
    path('<int:user_id>/rooms/update/action/<int:room_id>/', views.update_room_action, name='update_room_action')
]
