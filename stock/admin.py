import csv
import math
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.http import HttpResponse

from sitesettings.models import DollarExchangeRate, TransactionCoefficient
from .models import Inventory, Warehouse, StockMovement, Supplier, Purchase

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"

class InventoryAdmin(ModelAdmin, ExportCsvMixin):

    list_display = ['product', 'vat', 'warehouse', 'quantity', 'product__price', 'created', 'updated']
    search_fields = ['product__name', 'product__part_number']
    list_display_links = ['product', ]
    list_filter = (
        ('product__brand', admin.RelatedOnlyFieldListFilter),
        # ('product__type', admin.RelatedOnlyFieldListFilter),
        ('product__category', admin.RelatedOnlyFieldListFilter),
        ('warehouse', admin.RelatedOnlyFieldListFilter),
        'created',
        'quantity'
    )
    autocomplete_fields = ['product']
    actions = ["export_as_csv"]

    def product__price(self, obj):
        uzs_price = (obj.product.price * DollarExchangeRate.objects.filter().first().exchange_rate / TransactionCoefficient.objects.filter().first().coefficient)
        uzs_price = int(math.ceil(uzs_price / 1000)) * 1000
        uzs_price = '{:,.0f}'.format(uzs_price) + ' сум'
        return uzs_price

    def vat(self, obj):
        if obj.product.vat:
            vat = "НДС"
        else:
            vat = "Без НДС"
        return vat

admin.site.register(Inventory, InventoryAdmin)

class WarehouseAdmin(ModelAdmin):
    list_display = ['name', 'created', 'updated']
    list_display_links = ['name', ]
admin.site.register(Warehouse, WarehouseAdmin)

class StockMovementAdmin(ModelAdmin, ExportCsvMixin):
    list_display = ['product', 'from_warehouse', 'to_warehouse', 'quantity', 'moved_by', 'created', 'updated']
    list_display_links = ['product', ]
    search_fields = ['product__name', 'product__part_number']
    # search_fields = ['laptop__name', 'laptop__model']
    #list_editable = ['from_warehouse', 'to_warehouse', 'quantity', 'moved_by']
    exclude = ['moved_by']
    list_filter = (
        'created',
        ('moved_by', admin.RelatedOnlyFieldListFilter),
        ('from_warehouse', admin.RelatedOnlyFieldListFilter),
        ('to_warehouse', admin.RelatedOnlyFieldListFilter),
        ('product__brand', admin.RelatedOnlyFieldListFilter),
        ('product__category', admin.RelatedOnlyFieldListFilter),
        # ('laptop__screen_size', admin.RelatedOnlyFieldListFilter),
        # ('laptop__graphics_card', admin.RelatedOnlyFieldListFilter),
        # ('laptop__processor', admin.RelatedOnlyFieldListFilter),
    )
    autocomplete_fields = ['product']

    def save_model(self, request, obj, form, change):
        obj.moved_by = request.user
        super().save_model(request, obj, form, change)
admin.site.register(StockMovement, StockMovementAdmin)

class SupplierAdmin(ModelAdmin):
    list_display = ['name']
    def get_model_perms(self, request):
        # Hide from Admin panel, still allowing to use from inline
        return {}
admin.site.register(Supplier, SupplierAdmin)

class PurchaseAdmin(ModelAdmin, ExportCsvMixin):
    list_display = ['product', 'warehouse', 'cost', 'vat', 'supplier', 'quantity', 'created', 'updated']
    list_display_links = ['product', ]
    list_editable = ['warehouse', 'cost', 'quantity']
    search_fields = ['product__name']
    list_filter = (
        ('product__brand', admin.RelatedOnlyFieldListFilter),
        ('product__category', admin.RelatedOnlyFieldListFilter),
        ('supplier', admin.RelatedOnlyFieldListFilter),
        ('warehouse', admin.RelatedOnlyFieldListFilter),
        # ('warehouse', admin.RelatedOnlyFieldListFilter),
        ('created'),
    )
    autocomplete_fields = ['product']
    actions = ["export_as_csv"]

admin.site.register(Purchase, PurchaseAdmin)