from django.db import models


class ProcessorBrand(models.Model):
    """Processor Brand like Intel, AMD etc..."""
    name = models.CharField(max_length=30, help_text='К примеру: Intel Core или Intel Pentium')
    slug = models.SlugField(max_length=30)

    class Meta:
        verbose_name = 'Processor Brand'
        verbose_name_plural = 'Processor Brand'

    def __str__(self):
        return self.name
