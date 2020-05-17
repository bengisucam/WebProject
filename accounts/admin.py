from django.contrib import admin
from .models import User, Manager, Instructor, Customer

# Register your models here.

admin.site.register(User)
admin.site.register(Manager)
admin.site.register(Instructor)
admin.site.register(Customer)
