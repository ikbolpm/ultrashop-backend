from django.db import models

from processorBrand.models import ProcessorBrand


class Processor(models.Model):
    name = models.CharField(max_length=255, help_text='К примеру: i7-7700HQ')
    slug = models.SlugField(max_length=255)
    brand = models.ForeignKey(ProcessorBrand, on_delete=models.CASCADE, )
    min_frequency = models.FloatField(help_text='В ГГц. К примеру: 2.8')
    max_frequency = models.FloatField(help_text='В ГГЦ. К примеру: 3.8')
    cores = models.IntegerField(help_text='В шт. К примеру: 4')
    threads = models.IntegerField(help_text='В шт. К примеру: 8')
    cache = models.FloatField(help_text='В мегабайтах. К примеру: 6')
    integrated_graphics = models.CharField(max_length=255, help_text='К примеру: Intel® HD Graphics 630')

    def __str__(self):
        return self.name