from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import LaptopType, ComputerPerk, AllInOneType, DesktopType, PrinterTechnologyType, PrinterColorType, \
    PrinterFormat, PrinterFunction, PrinterPerks


class LaptopTypeAdmin (ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',), }


admin.site.register(LaptopType, LaptopTypeAdmin)


class AllIneOneTypeAdmin (ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',), }
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


admin.site.register(AllInOneType, AllIneOneTypeAdmin)


class DesktopTypeAdmin (ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',), }
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


admin.site.register(DesktopType, DesktopTypeAdmin)


class ComputerPerkAdmin(ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',), }


admin.site.register(ComputerPerk, ComputerPerkAdmin)


class PrinterColorTypeAdmin(ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',), }
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


admin.site.register(PrinterColorType, PrinterColorTypeAdmin)


class PrinterTechnologyTypeAdmin(ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',), }
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


admin.site.register(PrinterTechnologyType, PrinterTechnologyTypeAdmin)


class PrinterFunctionAdmin(ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',), }
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


admin.site.register(PrinterFunction, PrinterFunctionAdmin)


class PrinterFormatAdmin(ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',), }
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


admin.site.register(PrinterFormat, PrinterFormatAdmin)


class PrinterPerkAdmin(ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',), }
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


admin.site.register(PrinterPerks, PrinterPerkAdmin)