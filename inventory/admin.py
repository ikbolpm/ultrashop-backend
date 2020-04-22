import csv

from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.http import HttpResponse
from django.utils.safestring import mark_safe

from settings.models import DollarExchangeRate, TransactionCoefficient
import math


from .models import Inventory

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        # field_names = [field.name for field in meta.fields]
        field_names = ['laptop', 'vat', 'warehouse', 'quantity', 'laptop__price', 'created', 'updated']
        # field_names = field_names.append('laptop.price')

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"

class AvailableInventoryFilter(admin.SimpleListFilter):
    title = 'Available'
    parameter_name = 'squantity'

    def lookups(self, request, model_admin):
        return (
            ('Yes', 'Yes'),
            ('No', 'No'),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == 'Yes':
            return queryset.filter(quantity__gte=1)
        elif value == 'No':
            return queryset.filter(quantity__lte=0)
        return queryset


class InventoryAdmin(ModelAdmin, ExportCsvMixin):

    list_display = ['laptop', 'quantity', 'display_storefront_url', 'vat', 'warehouse', 'laptop__price', 'created', 'updated']

    def display_storefront_url(self, obj):
        return mark_safe('<a href="%s%s/%s/%s">%s</a>' % ('https://ultrashop.uz/', obj.laptop.brand.slug , obj.laptop.slug, obj.laptop.id, 'Link'))
    display_storefront_url.short_description = 'Link'
    search_fields = ['laptop__name', 'laptop__model', 'laptop__upc']
    list_display_links = ['laptop', ]
    list_filter = (
        AvailableInventoryFilter,
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

    # def laptop__price(self, obj):
    #     uzs_price = (obj.laptop.price * DollarExchangeRate.objects.filter().first().exchange_rate / TransactionCoefficient.objects.filter().first().coefficient)
    #     uzs_price = int(math.ceil(uzs_price / 1000)) * 1000
    #     uzs_price = '{:,.0f}'.format(uzs_price) + ' сум'
    #     return uzs_price
    #
    # def vat(self, obj):
    #     if obj.laptop.vat:
    #         vat = "НДС"
    #     else:
    #         vat = "Без НДС"
    #     return vat

admin.site.register(Inventory, InventoryAdmin)