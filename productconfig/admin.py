from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import LaptopType, LaptopPerks

class LaptopTypesAdmin (ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',), }

admin.site.register(LaptopType, LaptopTypesAdmin)

class LaptopPerksAdmin(ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',), }


admin.site.register(LaptopPerks, LaptopPerksAdmin)