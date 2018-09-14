from django.db import models

class Storage(models.Model):
    name = models.CharField(max_length=200, help_text='К примеру: SSD или HDD и т.д.')
    slug = models.SlugField(max_length=200)

    class Meta:
        verbose_name = 'Storage'
        verbose_name_plural = 'Storage'

    def __str__(self):
        return self.name
