from django.db import models
from ram.models import Ram


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    type = models.CharField(max_length=100)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.type = self.__class__.__name__

        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return "{} / {}".format(self.__class__.__name__, self.name)

class Laptop(Product):
    thumbnail = models.ImageField(upload_to='testing/thumbs', blank=True, null=True)


class Phone(Product):
    display = models.CharField(max_length=200)


class Inventory(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return "{} / {}".format(self.product.type, self.product.name)