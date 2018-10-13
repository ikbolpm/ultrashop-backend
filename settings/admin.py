from django.contrib import admin
from .models import DollarExchangeRate

class DollarExchangeRateAdmin(admin.ModelAdmin):
    list_display = ['exchange_rate', 'created', 'updated']

admin.site.register(DollarExchangeRate, DollarExchangeRateAdmin)
