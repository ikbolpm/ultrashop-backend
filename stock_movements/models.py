from django.db import models

from accounts.models import User
from inventory.models import Inventory
from laptop.models import Laptop
from warehouses.models import Warehouse


class StockMovements(models.Model):
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)
    from_warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='from_warehouse')
    to_warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='to_warehouse')
    quantity = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    moved_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Stock Movement',
        verbose_name_plural = 'Stock Movements'

    def __str__(self):
        return self.laptop.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
        inventory, moved_from = Inventory.objects.get_or_create(
            laptop=self.laptop,
            warehouse=self.from_warehouse,
            defaults={'quantity': 0}
        )
        inventory.quantity = inventory.quantity - self.quantity
        inventory.save()

        inventory, moved_to = Inventory.objects.get_or_create(
            laptop=self.laptop,
            warehouse=self.to_warehouse,
            defaults={'quantity': 0}
        )
        inventory.quantity = inventory.quantity + self.quantity
        inventory.save()
