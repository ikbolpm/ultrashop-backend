from django.db import models

class Resolution(models.Model):
    name = models.CharField(max_length=200, help_text='К примеру Full HD или QHD')
    slug = models.SlugField(max_length=200)
    size = models.CharField(max_length=200, help_text='К примеру 1920 х 1080')

    def __str__(self):
        return self.name