from django.db import models

class Audio(models.Model):
    name = models.CharField(max_length=200, help_text='К примеру: Bang & Olufsen Play')
    slug = models.SlugField(max_length=200)

    class Meta:
        verbose_name = 'Audio'
        verbose_name_plural = 'Audio'

    def __str__(self):
        return self.name
