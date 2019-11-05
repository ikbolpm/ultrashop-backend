from django.contrib import admin

from .models import Product, Laptop, Phone, Inventory

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    exclude = ['type']

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    exclude = ['type']

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    exclude = ['type']

