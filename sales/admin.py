from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Sales


class SalesAdmin(ModelAdmin):
    list_display = ['laptop', 'customer', 'warehouse', 'price', 'quantity', 'created', 'updated']
    list_display_links = ['laptop', ]
    list_editable = ['customer', 'warehouse', 'price', 'quantity', ]
    search_fields = ['customer', 'laptop', 'price']
    list_filter = ['laptop', 'customer', 'warehouse']


admin.site.register(Sales, SalesAdmin)