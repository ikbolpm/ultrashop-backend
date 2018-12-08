from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Customer


class CustomerAdmin(ModelAdmin):
    list_display = ['name', 'phone', 'email', 'created', 'updated']
    list_display_links = ['name', ]
    list_editable = ['phone', 'email']
    search_fields = ['name', 'phone', 'email']


admin.site.register(Customer, CustomerAdmin)
