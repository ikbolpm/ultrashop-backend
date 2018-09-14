from django.db import models

from laptop.models import Laptop
from warehouses.models import Warehouse


class Inventory(models.Model):
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, default=1)
    quantity = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Inventories'


    def __str__(self):
        return self.laptop.name
