from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import StockMovements


class StockMovementsAdmin(ModelAdmin):
    list_display = ['laptop', 'from_warehouse', 'to_warehouse', 'quantity', 'moved_by', 'created', 'updated']
    list_display_links = ['laptop', ]
    search_fields = ['laptop__name', 'laptop__model']
    list_editable = ['from_warehouse', 'to_warehouse', 'quantity', 'moved_by']
    exclude = ['moved_by']

    def save_model(self, request, obj, form, change):
        obj.moved_by = request.user
        super().save_model(request, obj, form, change)

admin.site.register(StockMovements, StockMovementsAdmin)
