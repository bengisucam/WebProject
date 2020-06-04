from django.urls import path
from . import views
from accounts.views import logoutPage

# seperate each app url individual files, dont overwhelm the WebProject/urls.py !

urlpatterns = [
    path('<int:user_id>/rooms/', views.list_myrooms, name='list_myrooms'),
    path('<int:user_id>/rooms/add/', views.add_room, name='add_room'),
    path('<int:user_id>/rooms/create/', views.create_room, name='create_room'),
    path('<int:user_id>/rooms/delete/<int:room_id>/', views.delete_room, name='delete_room'),
    path('<int:user_id>/rooms/update/<int:room_id>/', views.update_room, name='update_room'),
    path('<int:user_id>/rooms/update/action/<int:room_id>/', views.update_room_action, name='update_room_action'),
    path('<int:user_id>/ins/', views.list_ins, name='list_ins'),
    path('<int:user_id>/ins/add/', views.add_ins, name='add_ins'),
    path('<int:user_id>/ins/create/', views.create_ins, name='create_ins'),
    path('<int:user_id>/ins/delete/<int:ins_id>/', views.delete_ins, name='delete_ins'),
    path('<int:user_id>/ins/update/<int:ins_id>/', views.update_ins, name='update_ins'),
    path('<int:user_id>/ins/update/action/<int:ins_id>/', views.update_ins_action, name='update_ins_action'),
    path('<int:user_id>/pack/', views.list_pack, name='list_pack'),
    path('<int:user_id>/pack/add/', views.add_pack, name='add_pack'),
    path('<int:user_id>/pack/create/', views.create_pack, name='create_pack'),
    path('<int:user_id>/pack/delete/<int:pack_id>/', views.delete_pack, name='delete_pack'),
    path('<int:user_id>/pack/update/<int:pack_id>/', views.update_pack, name='update_pack'),
    path('<int:user_id>/pack/update/action/<int:pack_id>/', views.update_pack_action, name='update_pack_action'),
    path('<int:user_id>/pack/buy/<int:pack_id>/', views.buy_pack, name='buy_pack'),
    path('<int:user_id>/pack/myPacks/', views.my_packs, name='my_packs'),
    path('<int:user_id>/section/', views.list_section, name='list_section'),
    path('<int:user_id>/section/add/', views.add_section, name='add_section'),
    path('<int:user_id>/section/create/', views.create_section, name='create_section'),
    path('<int:user_id>/section/delete/<int:section_id>/', views.delete_section, name='delete_section'),
    path('<int:user_id>/section/update/<int:section_id>/', views.update_section, name='update_section'),
    path('<int:user_id>/section/update/action/<int:section_id>/', views.update_section_action,
         name='update_section_action'),
    path('<int:user_id>/member/', views.list_member, name='list_member'),
    path('<int:user_id>/schedule/', views.list_schedule, name='list_schedule'),
    path('<int:user_id>/profile/', views.show_profile, name='show_profile'),
    path('<int:user_id>/profile/changePassword/', views.change_password, name='change_password'),
    path('<int:user_id>/profile/changePassword/action', views.change_password_action, name='change_password_action'),
    path('<int:user_id>/logout/', logoutPage, name='logout'),

]
