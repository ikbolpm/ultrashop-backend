from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Lead


class LeadAdmin(ModelAdmin):
    list_display = ['name', 'phone_or_im', 'status', 'created', 'updated']
    list_display_links = ['name', ]
    list_editable = ['status']
    list_filter = ['status']
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


admin.site.register(Lead, LeadAdmin)
