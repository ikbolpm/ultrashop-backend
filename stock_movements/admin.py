from django.contrib import admin
from django.contrib.admin import ModelAdmin
from sales.admin import ExportCsvMixin

from .models import StockMovements


class StockMovementsAdmin(ModelAdmin, ExportCsvMixin):
    list_display = ['laptop', 'from_warehouse', 'to_warehouse', 'quantity', 'moved_by', 'created', 'updated']
    list_display_links = ['laptop', ]
    search_fields = ['laptop__name', 'laptop__model']
    # search_fields = ['laptop__name', 'laptop__model']
    #list_editable = ['from_warehouse', 'to_warehouse', 'quantity', 'moved_by']
    exclude = ['moved_by']
    list_filter = (
        'created',
        ('moved_by', admin.RelatedOnlyFieldListFilter),
        ('from_warehouse', admin.RelatedOnlyFieldListFilter),
        ('to_warehouse', admin.RelatedOnlyFieldListFilter),
        ('laptop__brand', admin.RelatedOnlyFieldListFilter),
        ('laptop__laptop_type', admin.RelatedOnlyFieldListFilter),
        ('laptop__screen_size', admin.RelatedOnlyFieldListFilter),
        ('laptop__graphics_card', admin.RelatedOnlyFieldListFilter),
        ('laptop__processor', admin.RelatedOnlyFieldListFilter),
    )
    autocomplete_fields = ['laptop']

    def save_model(self, request, obj, form, change):
        obj.moved_by = request.user
        super().save_model(request, obj, form, change)

admin.site.register(StockMovements, StockMovementsAdmin)