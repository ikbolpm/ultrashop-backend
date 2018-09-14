from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Resolution

class ResolutionAdmin(ModelAdmin):
    list_display = ['name', 'size']
    prepopulated_fields = {'slug': ('name',),}

admin.site.register(Resolution, ResolutionAdmin)