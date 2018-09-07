from django.db import models


class Warehouse(models.Model):
    name = models.CharField(max_length=255, help_text='Название склада/магазина')
    address = models.CharField(max_length=255, help_text='Адрес склада/магазина', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
