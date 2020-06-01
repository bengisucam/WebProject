from address.models import Address
from sportcenter.models import SportCenter
from django.db import models
# Create your models here.

YEARS = [x for x in range(1950, 2021)]
GENDERS = (
    ('FEMALE', 'Female'),
    ('MALE', 'Male')
)
ROLES = (
    ('MANAGER', 'Manager'),
    ('INSTRUCTOR', 'Instructor'),
    ('CUSTOMER', 'Customer')
)


class User(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    date_of_birth = models.DateField(blank=True)
    gender = models.CharField(max_length=6, choices=GENDERS)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=10, choices=ROLES, default=ROLES[1][1])
    sport_center_id = models.ForeignKey(SportCenter, blank=True, on_delete=models.CASCADE, null=True)
    address_id = models.ForeignKey(Address, blank=True, on_delete=models.CASCADE, null=True)

    services = models.ManyToManyField('sportcenter.Service', through='sportcenter.InstructorService')
    packages = models.ManyToManyField('sportcenter.Package', through='sportcenter.CustomerPackage')

