from django.contrib import admin

from .models import Inquiry, ProductInquiry

admin.site.site_header = ' UltraShop Admin Panel'

class InquiryAdmin(admin.ModelAdmin):
    list_display = [
        'laptop',
        'name',
        'phone',
        # 'min_price',
        # 'max_price',
        # 'min_cores',
        # 'max_cores',
        # 'min_size',
        # 'max_size',
        # 'min_storage',
        # 'max_storage',
        # 'min_ram',
        # 'max_ram',
        # 'source',
        'status',
        # 'description'
    ]
    list_display_links = ['laptop', ]
    # list_filter = ['source']
    autocomplete_fields = ['laptop']
    # def get_model_perms(self, request):
    #     """
    #     Return empty perms dict thus hiding the model from admin index.
    #     """
    #     return {}


admin.site.register(Inquiry, InquiryAdmin)


class ProductInquiryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'phone',
        'product',
        'source',
        'status',
        'description'
    ]
    list_display_links = ['product', 'status']
    list_filter = ['source']
    # def get_model_perms(self, request):
    #     """
    #     Return empty perms dict thus hiding the model from admin index.
    #     """
    #     return {}

admin.site.register(ProductInquiry, ProductInquiryAdmin)


