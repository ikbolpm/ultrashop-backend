from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Purchase


class PurchaseAdmin(ModelAdmin):
    list_display = ['laptop', 'warehouse', 'cost', 'quantity', 'created', 'updated']
    list_display_links = ['laptop', ]
    list_editable = ['warehouse', 'cost', 'quantity']
    list_filter = ['warehouse', 'laptop__brand', 'laptop__screen_size', 'laptop__graphics_card', 'laptop__processor']
    autocomplete_fields = ['laptop']

admin.site.register(Purchase, PurchaseAdmin)
