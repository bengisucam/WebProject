from django.shortcuts import render
from accounts.models import User
from sportcenter.models import Room

# Create your views here.

''' ROOM '''


def list_myrooms(request, user_id):
    active_user = User.objects.get(pk=user_id)
    rooms = Room.objects.all().filter(sport_center_id_id=active_user.sport_center_id_id)
    return render(request, 'sportcenter/list_myrooms.html', {'myrooms': rooms, 'active_user': active_user})


def add_room(request, user_id):
    active_user = User.objects.get(pk=user_id)
    return render(request, 'sportcenter/add_room.html', {'active_user': active_user})


def create_room(request, user_id):
    active_user = User.objects.get(pk=user_id)
    room_name = request.POST.get("room_name")
    room_capacity = request.POST.get("room_capacity")
    new_room = Room(room_name=room_name, room_capacity=room_capacity, sport_center_id_id=active_user.sport_center_id_id)
    new_room.save()
    return list_myrooms(request, user_id)


def delete_room(request, user_id, room_id):
    deleted_room = Room.objects.get(pk=room_id)
    deleted_room.delete()
    return list_myrooms(request, user_id)


def update_room(request, user_id, room_id):
    updated_room = Room.objects.get(pk=room_id)
    active_user = User.objects.get(pk=user_id)
    return render(request, 'sportcenter/update_room.html', {'active_user': active_user, 'update_room': updated_room})


def update_room_action(request, user_id, room_id):
    updated_room = Room.objects.get(pk=room_id)
    updated_room.room_name = request.POST.get("room_name")
    updated_room.room_capacity = request.POST.get("room_capacity")
    updated_room.save()
    return list_myrooms(request, user_id)


''' INSTRUCTOR '''
