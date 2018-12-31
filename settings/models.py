from django.db import models

class DollarExchangeRate(models.Model):
    exchange_rate = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.exchange_rate)

class TransactionCoefficient(models.Model):
    coefficient = models.DecimalField(max_digits=5, decimal_places=3)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)