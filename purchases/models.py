from django.db import models

from inventory.models import Inventory
from laptop.models import Laptop
from warehouses.models import Warehouse


class Purchase(models.Model):
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, default=1)
    quantity = models.IntegerField()
    cost = models.DecimalField(max_digits=7, decimal_places=2, help_text='Cost per each item, NOT total')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.laptop.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
        inventory, created = Inventory.objects.get_or_create(
            laptop=self.laptop,
            warehouse=self.warehouse,
            defaults={'quantity': 0}
        )
        inventory.quantity = self.quantity + inventory.quantity
        inventory.save()
