from django.contrib import admin
from django.contrib.admin import ModelAdmin
from sales.admin import ExportCsvMixin
from settings.models import DollarExchangeRate, TransactionCoefficient
import math


from .models import Inventory


class InventoryAdmin(ModelAdmin, ExportCsvMixin):

    list_display = ['laptop', 'vat', 'warehouse', 'quantity', 'laptop__price', 'created', 'updated']
    search_fields = ['laptop__name', 'laptop__model', 'laptop__upc']
    list_display_links = ['laptop', ]
    list_filter = (
        ('laptop__brand', admin.RelatedOnlyFieldListFilter),
        ('laptop__laptop_type', admin.RelatedOnlyFieldListFilter),
        ('laptop__screen_size', admin.RelatedOnlyFieldListFilter),
        ('laptop__resolution', admin.RelatedOnlyFieldListFilter),
        ('laptop__graphics_card', admin.RelatedOnlyFieldListFilter),
        ('laptop__processor', admin.RelatedOnlyFieldListFilter),
        ('laptop__perks', admin.RelatedOnlyFieldListFilter),
        ('warehouse', admin.RelatedOnlyFieldListFilter),
        'created',
    )
    autocomplete_fields = ['laptop']
    actions = ["export_as_csv"]

    def laptop__price(self, obj):
        uzs_price = (obj.laptop.price * DollarExchangeRate.objects.filter().first().exchange_rate / TransactionCoefficient.objects.filter().first().coefficient)
        uzs_price = int(math.ceil(uzs_price / 1000)) * 1000
        uzs_price = '{:,.0f}'.format(uzs_price) + ' сум'
        return uzs_price

    def vat(self, obj):
        if obj.laptop.vat:
            vat = "НДС"
        else:
            vat = "Без НДС"
        return vat

admin.site.register(Inventory, InventoryAdmin)