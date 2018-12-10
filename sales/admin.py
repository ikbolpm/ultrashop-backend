from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Sales


class SalesAdmin(ModelAdmin):
    list_display = ['laptop','serial_number', 'customer', 'warehouse', 'price', 'quantity', 'created', 'updated']
    list_display_links = ['laptop', ]
    list_editable = ['customer', 'warehouse', 'price', 'quantity', ]
    search_fields = ['customer__name', 'laptop__name', 'price']
    list_filter = ['warehouse']
    autocomplete_fields = ['laptop']

admin.site.register(Sales, SalesAdmin)