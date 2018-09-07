from django.db import models
from resolution.models import Resolution
from ram.models import Ram
from processorBrand.models import ProcessorBrand
from laptopType.models import LaptopType
from displaySize.models import DisplaySize
from storage.models import Storage
from laptop.models import Laptop

class Inquiry(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    comments = models.TextField(blank=True, null=True)
    size = models.ManyToManyField(DisplaySize, blank=True)
    ram = models.ManyToManyField(Ram, blank=True)
    laptop = models.ForeignKey(Laptop, blank=True, null=True, on_delete=models.CASCADE)
    resolution = models.ManyToManyField(Resolution, blank=True)
    storage = models.ManyToManyField(Storage, blank=True)
    type = models.ManyToManyField(LaptopType, blank=True)
    source = models.CharField(max_length=200)
    processor = models.ManyToManyField(ProcessorBrand, blank=True)
    min_price = models.CharField(max_length=50, blank=True, null=True)
    max_price = models.CharField(max_length=50, blank=True, null=True)
    min_cores = models.CharField(max_length=50, blank=True, null=True)
    max_cores = models.CharField(max_length=50, blank=True, null=True)
    min_size = models.CharField(max_length=4, blank=True, null=True)
    max_size = models.CharField(max_length=4, blank=True, null=True)
    min_storage = models.CharField(max_length=50, blank=True, null=True)
    max_storage = models.CharField(max_length=50, blank=True, null=True)
    min_ram = models.CharField(max_length=50, blank=True, null=True)
    max_ram = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Inquiries'

    def __str__(self):
        return self.name


