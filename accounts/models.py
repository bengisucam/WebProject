import uuid
from django import forms
from django.db import models

# Create your models here.


YEARS = [x for x in range(1950, 2021)]
GENDERS = (
    ('FEMALE', 'female'),
    ('MALE', 'male')
)
ROLES = (
    ('MANAGER', 'manager'),
    ('INSTRUCTOR', 'instructor'),
    ('CUSTOMER', 'customer')
)


class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
    gender = models.CharField(max_length=6, choices=GENDERS)
    email = models.EmailField()
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)
    is_active = models.BooleanField(blank=False)

    class Meta:
        abstract = False
        # ordering = ['first_name']


# bence bu 3 class gereksiz
class Manager(User):
    pass


class Instructor(User):
    pass


class Customer(User):
    pass


# user-role relation
class UserRole(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    role_name = models.CharField(max_length=10, choices=ROLES)