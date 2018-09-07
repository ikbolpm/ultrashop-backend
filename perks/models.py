from django.db import models

class Perks(models.Model):
    name = models.CharField(max_length=200, help_text='К примеру: Сенсорный экран')
    slug = models.SlugField(max_length=200)

    class Meta:
        verbose_name = 'Perks'
        verbose_name_plural = 'Perks'

    def __str__(self):
        return self.name
