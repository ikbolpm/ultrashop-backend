from django.contrib import admin

from .models import Inquiry

admin.site.site_header = ' UltraShop Admin Panel'

class InquiryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'phone',
        'laptop',
        'min_price',
        'max_price',
        'min_cores',
        'max_cores',
        'min_size',
        'max_size',
        'min_storage',
        'max_storage',
        'min_ram',
        'max_ram',
        'source',
    ]
    list_display_links = ['laptop', ]
    list_filter = ['source']

admin.site.register(Inquiry, InquiryAdmin)


