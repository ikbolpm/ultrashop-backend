from django.contrib import admin
from .models import Deal


class DealAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'active']
    search_fields = ['name']
    list_editable = ['active']
    save_as = True

admin.site.register(Deal, DealAdmin)