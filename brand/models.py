from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=200, help_text='К примеру: Asus, Acer, HP и т.д.')
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.name
