from django.contrib import admin
from django.contrib.admin import ModelAdmin
from sales.admin import ExportCsvMixin

from .models import Inventory


class InventoryAdmin(ModelAdmin, ExportCsvMixin):
    list_display = ['laptop', 'warehouse', 'quantity', 'created', 'updated']
    search_fields = ['laptop__name', 'laptop__model']
    list_display_links = ['laptop', ]
    list_editable = ['warehouse', 'quantity', ]
    list_filter = (
        ('laptop__brand', admin.RelatedOnlyFieldListFilter),
        ('laptop__screen_size', admin.RelatedOnlyFieldListFilter),
        ('laptop__graphics_card', admin.RelatedOnlyFieldListFilter),
        ('laptop__processor', admin.RelatedOnlyFieldListFilter),
        ('warehouse', admin.RelatedOnlyFieldListFilter),
        'created',
    )
    autocomplete_fields = ['laptop']
    actions = ["export_as_csv"]

admin.site.register(Inventory, InventoryAdmin)