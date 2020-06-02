from django.contrib import admin
from .models import Service
from .models import Package
from .models import Room
from .models import Section
from .models import SportCenter
from .models import CustomerPackage

# Register your models here.

admin.site.register(Service)
admin.site.register(Section)
admin.site.register(Package)
admin.site.register(Room)
admin.site.register(SportCenter)
admin.site.register(CustomerPackage)