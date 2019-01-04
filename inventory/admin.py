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
        ('warehouse', admin.RelatedOnlyFieldListFilter),
        ('laptop', admin.RelatedOnlyFieldListFilter),
    )
    autocomplete_fields = ['laptop']
    actions = ["export_as_csv"]


admin.site.register(Inventory, InventoryAdmin)
