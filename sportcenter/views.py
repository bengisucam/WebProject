import sys

from django.shortcuts import render
from accounts.models import User
from sportcenter.models import Room, Package, Service, PackageService, Section, CustomerPackage

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
    pack = Package.objects.filter(sport_center_id_id=active_user.sport_center_id_id)
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
    select = PackageService.objects.filter(package_id_id=pack_id)

    return render(request, 'sportcenter/update_pack.html',
                  {'active_user': active_user, 'update_pack': updated_pack, 'services': services,
                   'select_list': select})


def update_pack_action(request, user_id, pack_id):
    updated_pack = Package.objects.get(pk=pack_id)
    updated_pack.package_name = request.POST.get("pack_name")
    updated_pack.duration = request.POST.get("pack_duration")
    updated_pack.price = request.POST.get("pack_price")
    updated_pack.save()
    select = PackageService.objects.filter(package_id_id=pack_id)
    select.delete()
    for i in range(1, len(Service.objects.all()) + 1):
        if request.POST.get("check" + str(i)):
            new_package_service = PackageService(package_id_id=updated_pack.id, service_id_id=i)
            new_package_service.save()

    return list_pack(request, user_id)


'''         SECTION          '''


def list_section(request, user_id):
    active_user = User.objects.get(pk=user_id)
    section = Section.objects.select_related('instructor_id', 'room_id', 'service_id').filter(
        room_id__sport_center_id=active_user.sport_center_id_id)
    return render(request, 'sportcenter/list_section.html', {'section': section, 'active_user': active_user})


def add_section(request, user_id):
    active_user = User.objects.get(pk=user_id)
    instructor = User.objects.filter(sport_center_id_id=active_user.sport_center_id_id, role='Instructor')
    room = Room.objects.filter(sport_center_id_id=active_user.sport_center_id_id)
    service = Service.objects.all()
    return render(request, 'sportcenter/add_section.html',
                  {'active_user': active_user, 'instructor': instructor, 'room': room, 'service': service})


def create_section(request, user_id):
    section_name = request.POST.get("section_name")
    section_start = request.POST.get("section_start")
    section_end = request.POST.get("section_end")
    section_day = request.POST.get("section_day")
    section_ins_id = request.POST.get("section_ins")
    section_room_id = request.POST.get("section_room")
    section_service_id = request.POST.get("section_service")
    new_section = Section(section_name=section_name, start_time=section_start, end_time=section_end,
                          section_day=section_day, instructor_id_id=section_ins_id, room_id_id=section_room_id,
                          service_id_id=section_service_id)

    new_section.save()
    return list_section(request, user_id)


def delete_section(request, user_id, section_id):
    deleted_section = Section.objects.get(pk=section_id)
    deleted_section.delete()
    return list_section(request, user_id)


def update_section(request, user_id, section_id):
    active_user = User.objects.get(pk=user_id)
    instructor = User.objects.filter(sport_center_id_id=active_user.sport_center_id_id, role='Instructor')
    room = Room.objects.filter(sport_center_id_id=active_user.sport_center_id_id)
    service = Service.objects.all()
    updated_section = Section.objects.get(pk=section_id)

    return render(request, 'sportcenter/update_section.html',
                  {'active_user': active_user, 'update_section': updated_section, 'instructor': instructor,
                   'room': room, 'service': service})


def update_section_action(request, user_id, section_id):
    updated_section = Section.objects.get(pk=section_id)
    updated_section.section_name = request.POST.get("section_name")
    # updated_section.start_time = request.POST.get("section_start")
    # updated_section.end_time = request.POST.get("section_end")
    updated_section.instructor_id_id = request.POST.get("section_ins")
    updated_section.room_id_id = request.POST.get("section_room")
    updated_section.service_id_id = request.POST.get("section_service")
    updated_section.save()
    return list_section(request, user_id)


'''         MEMBER          '''


def list_member(request, user_id):
    active_user = User.objects.get(pk=user_id)
    member_package = CustomerPackage.objects.prefetch_related('customer_id', 'package_id').filter(
        package_id__sport_center_id=active_user.sport_center_id_id).order_by('-begin_date')
    return render(request, 'sportcenter/list_member.html',
                  {'active_user': active_user, 'member_package': member_package})


'''         INSTRUCTOR SCHEDUL          '''


def list_schedule(request, user_id):
    active_user = User.objects.get(pk=user_id)
    section_ins = Section.objects.select_related('instructor_id').filter(instructor_id_id=active_user.id)
    return render(request, 'sportcenter/list_schedule.html',
                  {'active_user': active_user, 'section_ins': section_ins})
