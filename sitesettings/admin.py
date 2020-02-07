from django.contrib import admin
from .models import DollarExchangeRate, TransactionCoefficient


class DollarExchangeRateAdmin(admin.ModelAdmin):
    list_display = ['exchange_rate', 'created', 'updated']
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

admin.site.register(DollarExchangeRate, DollarExchangeRateAdmin)


class TransactionCoefficientAdmin(admin.ModelAdmin):
    list_display = ['coefficient', 'created', 'updated']
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

admin.site.register(TransactionCoefficient, TransactionCoefficientAdmin)