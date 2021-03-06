from django.db import models

class LaptopType(models.Model):
    name = models.CharField(max_length=200, help_text='Во множественном числе. К примеру: УльтрабукИ, трансформеры и т.д.')
    slug = models.SlugField(max_length=200)
    name_singular = models.CharField(max_length=200, help_text='В единственном числе. К примеру: Ультрабук, трансформер и т.д.')
    short_description = models.TextField(default="Ultrabuki")
    logo = models.ImageField(upload_to='laptop-types', default='default.png')
    isLaptop = models.BooleanField()

    class Meta:
        verbose_name = 'Laptop Type'

    def __str__(self):
        return self.name