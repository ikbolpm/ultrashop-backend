import math

from django.db import models

from laptop.models import Laptop
from settings.models import DollarExchangeRate, TransactionCoefficient
from warehouses.models import Warehouse


class Inventory(models.Model):
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, default=1)
    quantity = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Inventories'
        unique_together = ['laptop', 'warehouse']


    def __str__(self):
        return self.laptop.name

    @property
    def laptop__price(self):
        uzs_price = (self.laptop.price * DollarExchangeRate.objects.filter().first().exchange_rate / TransactionCoefficient.objects.filter().first().coefficient)
        uzs_price = int(math.ceil(uzs_price / 1000)) * 1000
        uzs_price = '{:,.0f}'.format(uzs_price)
        return uzs_price

    @property
    def vat(self):
        if self.laptop.vat:
            vat = "Yes"
        else:
            vat = "No"
        return vat
