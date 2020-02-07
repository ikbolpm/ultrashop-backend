from django.contrib import admin
from .models import Deal


class DealAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'active']
    search_fields = ['name']
    list_editable = ['active']
    save_as = True
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

admin.site.register(Deal, DealAdmin)