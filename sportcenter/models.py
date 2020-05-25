import uuid
from django import forms
from django.db import models


# Create your models here.
class SportCenter(models.Model):
    sport_center_name = models.CharField(max_length=100, blank=False)
    opening_time = models.TimeField(auto_now=False)
    closing_time = models.TimeField(auto_now=False)


class Package(models.Model):
    package_name = models.CharField(max_length=100, blank=False)
    price = models.IntegerField()
    duration = models.IntegerField()


class Room(models.Model):
    room_name = models.CharField(max_length=100, blank=False)
    room_capacity = models.IntegerField()


class Service(models.Model):
    service_name = models.CharField(max_length=100, blank=False)


class Section(models.Model):
    section_name = models.CharField(max_length=100, blank=False)
    start_time = models.TimeField(auto_now=False)
    end_time = models.TimeField(auto_now=False)
