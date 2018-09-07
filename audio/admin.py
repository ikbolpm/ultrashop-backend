from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Audio

class AudioAdmin(ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',), }


admin.site.register(Audio, AudioAdmin)
