from django.contrib import admin
from .models import Destination, bank, cars
# Register your models here.

admin.site.register(cars)
admin.site.register(bank)