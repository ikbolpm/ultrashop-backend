from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Inventory


class InventoryAdmin(ModelAdmin):
    list_display = ['laptop', 'warehouse', 'quantity', 'created', 'updated']
    list_display_links = ['laptop', ]
    list_editable = ['warehouse', 'quantity', ]
    list_filter = ['warehouse', 'laptop']


admin.site.register(Inventory, InventoryAdmin)
