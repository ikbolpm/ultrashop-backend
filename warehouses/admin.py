from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Warehouse


class WarehouseAdmin(ModelAdmin):
    list_display = ['name', 'address', 'created', 'updated']
    list_display_links = ['name', ]
    list_editable = ['address']


admin.site.register(Warehouse, WarehouseAdmin)
