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


def list_ins(request, user_id):
    active_user = User.objects.get(pk=user_id)
    ins = User.objects.all().filter(sport_center_id_id=active_user.sport_center_id_id, role='Instructor')
    return render(request, 'sportcenter/list_ins.html', {'ins': ins, 'active_user': active_user})


def add_ins(request, user_id):
    active_user = User.objects.get(pk=user_id)
    return render(request, 'sportcenter/add_ins.html', {'active_user': active_user})


def create_ins(request, user_id):
    active_user = User.objects.get(pk=user_id)
    ins_first_name = request.POST.get("ins_first_name")
    ins_last_name = request.POST.get("ins_first_name")
    ins_date = request.POST.get("ins_date")
    ins_gender = request.POST.get("ins_gender")
    ins_email = request.POST.get("ins_email")
    ins_password = request.POST.get("ins_password")
    new_ins = User(first_name=ins_first_name, last_name=ins_last_name, date_of_birth=ins_date, gender=ins_gender,
                   email=ins_email, password=ins_password, role='Instructor',
                   sport_center_id_id=active_user.sport_center_id_id)
    new_ins.save()
    return list_ins(request, user_id)


def delete_ins(request, user_id, ins_id):
    deleted_ins = User.objects.get(pk=ins_id)
    deleted_ins.delete()
    return list_ins(request, user_id)


def update_ins(request, user_id, ins_id):
    updated_ins = User.objects.get(pk=ins_id)
    active_user = User.objects.get(pk=user_id)
    return render(request, 'sportcenter/update_ins.html', {'active_user': active_user, 'update_ins': updated_ins})


def update_ins_action(request, user_id, ins_id):
    updated_ins = User.objects.get(pk=ins_id)
    updated_ins.first_name = request.POST.get("ins_first_name")
    updated_ins.last_name = request.POST.get("ins_last_name")
    #updated_ins.date_of_birth = request.POST.get("ins_date")
    #updated_ins.gender = request.POST.get("ins_gender")
    updated_ins.email = request.POST.get("ins_email")
    updated_ins.password = request.POST.get("ins_password")
    updated_ins.save()
    return list_ins(request, user_id)
