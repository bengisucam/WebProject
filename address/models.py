from django.db import models


# Create your models here.
class Country(models.Model):
    country_name = models.CharField(max_length=30, blank=False)


class City(models.Model):
    city_name = models.CharField(max_length=30, blank=False)
    country_id = models.ForeignKey(Country, blank=True, on_delete=models.CASCADE)


class Address(models.Model):
    address_name = models.CharField(max_length=100, blank=False)
    zip_code = models.IntegerField(blank=True)
    city_id = models.ForeignKey(City, blank=True, on_delete=models.CASCADE)

