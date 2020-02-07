from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Audio

class AudioAdmin(ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',), }
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


admin.site.register(Audio, AudioAdmin)
