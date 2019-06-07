import csv

from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.http import HttpResponse

from .models import Sales, CustomerReturns

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

class SalesAdmin(ModelAdmin, ExportCsvMixin):
    list_display = ['laptop', 'customer', 'sold_by', 'warehouse', 'price', 'profit', 'quantity', 'created']
    list_display_links = ['laptop', ]
    search_fields = ['customer__name', 'laptop__name', 'price', ]
    actions = ["export_as_csv"]

    list_filter = (
        ('created'),
        ('laptop__brand', admin.RelatedOnlyFieldListFilter),
        ('laptop__screen_size', admin.RelatedOnlyFieldListFilter),
        ('laptop__graphics_card', admin.RelatedOnlyFieldListFilter),
        ('laptop__processor', admin.RelatedOnlyFieldListFilter),
        ('warehouse', admin.RelatedOnlyFieldListFilter),
        ('sold_by', admin.RelatedOnlyFieldListFilter),
    )
    autocomplete_fields = ['laptop', 'customer']
    exclude = ['sold_by']

    # def laptop__brand(self, obj):
    #     laptop__brand = obj.laptop.brand.name
    #     return laptop__brand
    #
    # def laptop__processor(self, obj):
    #     laptop__processor = obj.laptop.processor.name
    #     return laptop__processor
    #
    # def laptop__screen(self, obj):
    #     laptop__screen = obj.laptop.screen_size
    #     return laptop__screen
    #
    # def laptop__graphics(self, obj):
    #     laptop__graphics = obj.laptop.graphics_card
    #     return laptop__graphics

    def save_model(self, request, obj, form, change):
        obj.sold_by = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Sales, SalesAdmin)


class CustomerReturnsAdmin(ModelAdmin, ExportCsvMixin):
    list_display = ['laptop', 'received_by', 'warehouse', 'reason', 'quantity', 'created']
    list_display_links = ['laptop', ]
    search_fields = ['laptop__name', 'reason', ]
    actions = ["export_as_csv"]

    list_filter = (
        ('created'),
        ('laptop__brand', admin.RelatedOnlyFieldListFilter),
        ('laptop__screen_size', admin.RelatedOnlyFieldListFilter),
        ('laptop__graphics_card', admin.RelatedOnlyFieldListFilter),
        ('laptop__processor', admin.RelatedOnlyFieldListFilter),
        ('warehouse', admin.RelatedOnlyFieldListFilter),
        ('received_by', admin.RelatedOnlyFieldListFilter),
    )
    autocomplete_fields = ['laptop']
    exclude = ['received_by']

    def save_model(self, request, obj, form, change):
        obj.received_by = request.user
        super().save_model(request, obj, form, change)

admin.site.register(CustomerReturns, CustomerReturnsAdmin)