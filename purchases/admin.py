from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Purchase


class PurchaseAdmin(ModelAdmin):
    list_display = ['laptop', 'warehouse', 'cost', 'quantity', 'created', 'updated']
    list_display_links = ['laptop', ]
    list_editable = ['warehouse', 'cost', 'quantity']
    list_filter = ['warehouse', 'laptop']
    autocomplete_fields = ['laptop']

admin.site.register(Purchase, PurchaseAdmin)
