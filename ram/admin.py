from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Ram

class RamAdmin(ModelAdmin):
    list_display = ['generation']
    prepopulated_fields = {'slug': ('generation',), }
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

admin.site.register(Ram, RamAdmin)
