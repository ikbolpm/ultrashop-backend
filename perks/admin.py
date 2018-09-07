from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Perks

class PerksAdmin(ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',), }


admin.site.register(Perks, PerksAdmin)
