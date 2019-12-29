from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
from shop.models import Product


class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    warehouse = models.ForeignKey('Warehouse', on_delete=models.CASCADE, default=1)
    quantity = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Inventories'
        unique_together = ['product', 'warehouse']

    def __str__(self):
        return "{} / {}".format(self.product.type, self.product.name)


class Warehouse(models.Model):
    name = models.CharField(max_length=255, help_text='Название склада/магазина')
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class StockMovement(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    from_warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='from_warehouse')
    to_warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='to_warehouse')
    quantity = models.IntegerField()
    comments = models.TextField(blank=True, null=True,
                                help_text='Дополнительные комментарии. Например кому отдали, за сколько и т.д.')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    moved_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Stock Movement',
        verbose_name_plural = 'Stock Movements'

    def __str__(self):
        return self.product.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
        inventory, moved_from = Inventory.objects.get_or_create(
            product=self.product,
            warehouse=self.from_warehouse,
            defaults={'quantity': 0}
        )
        inventory.quantity = inventory.quantity - self.quantity
        inventory.save()

        inventory, moved_to = Inventory.objects.get_or_create(
            product=self.product,
            warehouse=self.to_warehouse,
            defaults={'quantity': 0}
        )
        inventory.quantity = inventory.quantity + self.quantity
        inventory.save()


class Supplier(models.Model):
    name = models.CharField(max_length=255, help_text='CA Distribution')

    def __str__(self):
        return self.name


class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)
    warehouse = models.ForeignKey('Warehouse', on_delete=models.CASCADE, default=1)
    quantity = models.IntegerField()
    cost = models.DecimalField(max_digits=7, decimal_places=2, help_text='Cost per each item, NOT total')
    vat = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        new_creation = False
        if not self.id:
            new_creation = True
        super().save(force_insert, force_update, using, update_fields)
        if new_creation:
            inventory, created = Inventory.objects.get_or_create(
                product=self.product,
                warehouse=self.warehouse,
                defaults={'quantity': 0}
            )
            inventory.quantity = self.quantity + inventory.quantity
            inventory.save()