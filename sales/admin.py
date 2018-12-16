from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Sales


class SalesAdmin(ModelAdmin):
    list_display = ['laptop','profit']
    list_display_links = ['laptop', ]
    list_editable = ['profit']
    # search_fields = ['customer__name', 'laptop__name', 'price']
    # list_filter = ['warehouse', 'sold_by']
    autocomplete_fields = ['laptop']

admin.site.register(Sales, SalesAdmin)