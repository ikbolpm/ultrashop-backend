from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Sales


class SalesAdmin(ModelAdmin):
    list_display = ['laptop', 'customer', 'sold_by', 'warehouse', 'price', 'profit', 'quantity', 'created']
    list_display_links = ['laptop', ]
    # list_editable = ['customer', 'warehouse', 'price', 'quantity', ]
    search_fields = ['customer__name', 'laptop__name', 'price']
    list_filter = ['warehouse', 'sold_by']
    autocomplete_fields = ['laptop']
    exclude = ['sold_by']

admin.site.register(Sales, SalesAdmin)