from django.contrib import admin
from django.contrib.admin import ModelAdmin
from brand.models import Brand

from .models import Inventory


class InventoryAdmin(ModelAdmin):
    list_display = ['laptop', 'warehouse', 'quantity', 'created', 'updated']
    search_fields = ['laptop__name', 'laptop__model']
    list_display_links = ['laptop', ]
    list_editable = ['warehouse', 'quantity', ]
    list_filter = (
        ('warehouse', admin.RelatedOnlyFieldListFilter),
        ('laptop', admin.RelatedOnlyFieldListFilter),
    )


admin.site.register(Inventory, InventoryAdmin)
