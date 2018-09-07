from django.db import models

from customers.models import Customer
from inventory.models import Inventory
from laptop.models import Laptop
from warehouses.models import Warehouse


class Sales(models.Model):
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, default=1)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Sales'
        verbose_name = 'Sale'

    def __str__(self):
        return self.laptop.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
        inventory, created = Inventory.objects.get_or_create(
            laptop=self.laptop,
            warehouse=self.warehouse,
            defaults={'quantity': 0}
        )
        inventory.quantity = inventory.quantity - self.quantity
        inventory.save()