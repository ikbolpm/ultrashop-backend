from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import DisplaySize

class DisplaySizeAdmin(ModelAdmin):
    list_display = ['size']
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

admin.site.register(DisplaySize, DisplaySizeAdmin)