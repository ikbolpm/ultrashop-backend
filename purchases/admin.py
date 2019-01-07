from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Purchase


class PurchaseAdmin(ModelAdmin):
    list_display = ['laptop', 'warehouse', 'cost', 'quantity', 'created', 'updated']
    list_display_links = ['laptop', ]
    list_editable = ['warehouse', 'cost', 'quantity']
    list_filter = (
        ('laptop__brand', admin.RelatedOnlyFieldListFilter),
        ('laptop__screen_size', admin.RelatedOnlyFieldListFilter),
        ('laptop__graphics_card', admin.RelatedOnlyFieldListFilter),
        ('laptop__processor', admin.RelatedOnlyFieldListFilter),
        ('warehouse', admin.RelatedOnlyFieldListFilter),
        ('created'),
    )
    autocomplete_fields = ['laptop']

admin.site.register(Purchase, PurchaseAdmin)
