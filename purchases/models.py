from django.db import models
from inventory.models import Inventory
from laptop.models import Laptop
from warehouses.models import Warehouse


class Purchase(models.Model):
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, default=1)
    quantity = models.IntegerField()
    country = models.ForeignKey("Country", blank=True, null=True, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=7, decimal_places=2, help_text='Cost per each item, NOT total')
    vat = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.laptop.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        new_creation = False
        if not self.id:
            new_creation = True
        super().save(force_insert, force_update, using, update_fields)
        if new_creation:
            inventory, created = Inventory.objects.get_or_create(
                laptop=self.laptop,
                warehouse=self.warehouse,
                defaults={'quantity': 0}
            )
            inventory.quantity = self.quantity + inventory.quantity
            inventory.save()


class Country(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name