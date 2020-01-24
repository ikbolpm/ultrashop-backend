import csv

from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.http import HttpResponse

from .models import Purchase, Country


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


class PurchaseAdmin(ModelAdmin, ExportCsvMixin):
    list_display = ['laptop', 'vat', 'country', 'quantity', 'created', 'updated', 'warehouse']
    list_display_links = ['laptop', ]
    list_editable = ['country', 'vat']
    search_fields = ['laptop__name', 'laptop__upc', 'laptop__model']
    list_filter = (
        ('laptop__brand', admin.RelatedOnlyFieldListFilter),
        ('laptop__screen_size', admin.RelatedOnlyFieldListFilter),
        ('laptop__graphics_card', admin.RelatedOnlyFieldListFilter),
        ('laptop__processor', admin.RelatedOnlyFieldListFilter),
        ('warehouse', admin.RelatedOnlyFieldListFilter),
        ('created'),
    )
    autocomplete_fields = ['laptop']
    actions = ["export_as_csv"]


admin.site.register(Purchase, PurchaseAdmin)


class CountryAdmin(ModelAdmin):
    list_display = ['name']


admin.site.register(Country, CountryAdmin)


