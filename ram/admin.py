from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Ram

class RamAdmin(ModelAdmin):
    list_display = ['generation']
    prepopulated_fields = {'slug': ('generation',), }

admin.site.register(Ram, RamAdmin)
