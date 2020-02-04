from django.contrib import admin
from .models import Order, OrderItem, Inquiry


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    autocomplete_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'warehouse', 'price', 'created', 'updated']
    list_filter = ('created', 'warehouse')
    inlines = [OrderItemInline]
    autocomplete_fields = ['customer']
    save_as = True


class InquiryAdmin(admin.ModelAdmin):
    list_display = ['inquired_product', 'name', 'phone', 'status', 'created', ]
    list_display_links = ['inquired_product',]
    list_filter = ('created', 'status', )
    autocomplete_fields = ('sold_product',)
admin.site.register(Inquiry, InquiryAdmin)