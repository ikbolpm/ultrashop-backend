from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import DisplaySize

class DisplaySizeAdmin(ModelAdmin):
    list_display = ['size']


admin.site.register(DisplaySize, DisplaySizeAdmin)