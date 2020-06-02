import sys

from django.db.models import Count
from django.shortcuts import render, redirect
from accounts.models import User
from sportcenter.models import Room, Package, Service, PackageService, CustomerPackage

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
    # updated_ins.date_of_birth = request.POST.get("ins_date")
    # updated_ins.gender = request.POST.get("ins_gender")
    updated_ins.email = request.POST.get("ins_email")
    updated_ins.password = request.POST.get("ins_password")
    updated_ins.save()
    return list_ins(request, user_id)


''' PACKAGE '''


def list_pack(request, user_id):
    active_user = User.objects.get(pk=user_id)
    if (active_user.role == 'Manager'):
        pack = Package.objects.filter(sport_center_id_id=active_user.sport_center_id_id)
    else:
        pack = Package.objects.all()
    pack_service = PackageService.objects.select_related('service_id')
    return render(request, 'sportcenter/list_pack.html',
                  {'pack': pack, 'active_user': active_user, 'pack_service': pack_service})


def add_pack(request, user_id):
    active_user = User.objects.get(pk=user_id)
    services = Service.objects.all()
    return render(request, 'sportcenter/add_pack.html', {'active_user': active_user, 'services': services})


def create_pack(request, user_id):
    active_user = User.objects.get(pk=user_id)
    pack_name = request.POST.get("pack_name")
    pack_duration = request.POST.get("pack_duration")
    pack_price = request.POST.get("pack_price")
    new_package = Package(package_name=pack_name, duration=pack_duration, price=pack_price,
                          sport_center_id_id=active_user.sport_center_id_id)
    new_package.save()

    for i in range(1, len(Service.objects.all()) + 1):
        if request.POST.get("check" + str(i)):
            new_package_service = PackageService(package_id_id=new_package.id, service_id_id=i)
            new_package_service.save()

    return list_pack(request, user_id)


def delete_pack(request, user_id, pack_id):
    deleted_pack = Package.objects.get(pk=pack_id)
    deleted_pack.delete()
    return list_pack(request, user_id)


def update_pack(request, user_id, pack_id):
    updated_pack = Package.objects.get(pk=pack_id)
    active_user = User.objects.get(pk=user_id)
    services = Service.objects.all()
    select = PackageService.objects.filter(package_id_id=pack_id).select_related('service_id_id')

    return render(request, 'sportcenter/update_pack.html',
                  {'active_user': active_user, 'update_pack': updated_pack, 'services': services, 'select': select})


def update_pack_action(request, user_id, pack_id):
    updated_pack = Package.objects.get(pk=pack_id)
    updated_pack.package_name = request.POST.get("pack_name")
    updated_pack.duration = request.POST.get("pack_duration")
    updated_pack.price = request.POST.get("pack_price")
    for i in range(1, len(Service.objects.all()) + 1):
        if request.POST.get("check" + str(i)):
            new_package_service = PackageService.objects.filter(package_id_id=pack_id)
            new_package_service.save()

    updated_pack.save()
    return list_ins(request, user_id)


def buy_pack(request, user_id, pack_id):
    selected_pack = Package.objects.get(pk=pack_id)
    active_user = User.objects.get(pk=user_id)
    new_customer_pack = CustomerPackage(selected_pack,active_user)
    new_customer_pack.save()
    # pack = CustomerPackage.objects.filter(customer_id_id=active_user).select_related('package_id_id')
    return redirect('list_pack')


def my_packs(request, user_id):
    active_user = User.objects.get(pk=user_id)
    pack = CustomerPackage.objects.filter(customer_id_id=active_user)
    return render(request, 'sportcenter/my_packs.html',
                  {'pack': pack, 'active_user': active_user})