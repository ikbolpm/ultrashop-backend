from django.contrib import admin
from .models import DollarExchangeRate, TransactionCoefficient


class DollarExchangeRateAdmin(admin.ModelAdmin):
    list_display = ['exchange_rate', 'created', 'updated']

admin.site.register(DollarExchangeRate, DollarExchangeRateAdmin)


class TransactionCoefficientAdmin(admin.ModelAdmin):
    list_display = ['coefficient', 'created', 'updated']

admin.site.register(TransactionCoefficient, TransactionCoefficientAdmin)