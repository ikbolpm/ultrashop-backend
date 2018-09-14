from django.db import models

class GraphicsCardBrand(models.Model):
    name = models.CharField(max_length=250, help_text='К примеру: nVidia')
    slug = models.SlugField(max_length=200)

    class Meta:
        verbose_name = 'Graphics Card Brand'
        verbose_name_plural = 'Graphics Card Brands'

    def __str__(self):
        return self.name
