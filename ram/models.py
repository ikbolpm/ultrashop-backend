from django.db import models

class Ram(models.Model):
    generation = models.CharField(max_length=20, help_text='К примеру: DDR 4')
    slug = models.SlugField(max_length=20)

    class Meta:
        verbose_name = 'RAM'
        verbose_name_plural = 'RAM'

    def __str__(self):
        return self.generation