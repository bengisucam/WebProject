from django.db import models

# Create your models here.
from address.models import Address


# from accounts.models import User


class SportCenter(models.Model):
    sport_center_name = models.CharField(max_length=100, blank=False)
    opening_time = models.TimeField(auto_now=False)
    closing_time = models.TimeField(auto_now=False)
    address_id = models.ForeignKey(Address, blank=True, on_delete=models.CASCADE)


class Package(models.Model):
    package_name = models.CharField(max_length=100, blank=False)
    price = models.IntegerField()
    duration = models.IntegerField()
    sport_center_id = models.ForeignKey(SportCenter, on_delete=models.CASCADE)


class Room(models.Model):
    room_name = models.CharField(max_length=100, blank=False)
    room_capacity = models.IntegerField()
    sport_center_id = models.ForeignKey(SportCenter, on_delete=models.CASCADE)


class Service(models.Model):
    service_name = models.CharField(max_length=100, blank=False)


class Section(models.Model):
    section_name = models.CharField(max_length=100, blank=False)
    start_time = models.TimeField(auto_now=False)
    end_time = models.TimeField(auto_now=False)
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    instructor_id = models.ForeignKey("accounts.User", on_delete=models.CASCADE)


class CustomerPackage(models.Model):
    customer_id = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    package_id = models.ForeignKey(Package, on_delete=models.CASCADE)
    begin_date = models.DateTimeField(auto_now_add=True, blank=True)


class PackageService(models.Model):
    package_id = models.ForeignKey(Package, on_delete=models.CASCADE)
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE)


class InstructorService(models.Model):
    instructor_id = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE)
