from django.contrib import admin
from .models import Car
from .models import Provider
# Register your models here.

@admin.register(Car)

class CarAdmin(admin.ModelAdmin):
    list_display = ('car_brand', 'provider','price')
    search_fields = ['car_brand__istartswith']

@admin.register(Provider)

class ProviderAdmin(admin.ModelAdmin):
    list_display = ('provider', 'email')
    List_filter = ['provider']