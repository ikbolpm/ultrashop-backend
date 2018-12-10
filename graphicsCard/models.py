from django.db import models
from graphicsCardBrand.models import GraphicsCardBrand

class GraphicsCard(models.Model):
    name = models.CharField(max_length=250, help_text='К примеру: GeForce GTX 1060')
    slug = models.SlugField(max_length=250)
    brand = models.ForeignKey(GraphicsCardBrand, on_delete=models.CASCADE, )
    memory_interface = models.CharField(max_length=20, help_text='К примеру: GDDR5')
    memory_interface_width = models.IntegerField(help_text='В битах. К примеру: 128')

    class Meta:
        verbose_name_plural = 'Graphics Cards'
        verbose_name = 'Graphics Card'
        ordering = ['name']
        unique_together = ['name', 'brand']

    def __str__(self):
        return self.name
