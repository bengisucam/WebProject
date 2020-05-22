import uuid
from django import forms
from django.db import models


# Create your models here.
class SportCenter(models.Model):
    sport_center_id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    sport_center_name = models.CharField(max_length=100, blank=False)
    opening_time = models.TimeField(auto_now=False)
    closing_time = models.TimeField(auto_now=False)


class Package(models.Model):
    package_id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    package_name = models.CharField(max_length=100, blank=False)
    price = models.IntegerField()
    duration = models.IntegerField()


class Room(models.Model):
    room_id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    room_name = models.CharField(max_length=100, blank=False)
    room_capacity = models.IntegerField()


class Service(models.Model):
    service_id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    service_name = models.CharField(max_length=100, blank=False)


class Section(models.Model):
    section_id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    section_name = models.CharField(max_length=100, blank=False)
    start_time = models.TimeField(auto_now=False)
    end_time = models.TimeField(auto_now=False)
