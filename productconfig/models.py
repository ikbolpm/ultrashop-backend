from django.db import models


class ComputerType(models.Model):
    name = models.CharField(max_length=200,
                            help_text='Во множественном числе. К примеру: УльтрабукИ, трансформеры и т.д.')
    slug = models.SlugField(max_length=200)
    name_singular = models.CharField(max_length=200,
                                     help_text='В единственном числе. К примеру: Ультрабук, трансформер и т.д.')
    short_description = models.TextField(null=True, blank=True)
    logo = models.ImageField(upload_to='laptop-types', default='default.png')

    def __str__(self):
        return self.name


class LaptopType(ComputerType):
    pass


class AllInOneType(ComputerType):
    pass


class DesktopType(ComputerType):
    pass


class ComputerPerk(models.Model):
    name = models.CharField(max_length=200, help_text='К примеру: Сенсорный экран')
    slug = models.SlugField(max_length=200)

    class Meta:
        verbose_name = 'Laptop Perks'
        verbose_name_plural = 'Laptop Perks'
        ordering = ['name']

    def __str__(self):
        return self.name


class PrinterConfig(models.Model):
    name = models.CharField(max_length=200, help_text='К примеру: Черно-белый или Цветной')
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.name

class PrinterColorType(PrinterConfig):
    pass


class PrinterTechnologyType(PrinterConfig):
    pass


class PrinterFunction(PrinterConfig):
    pass


class PrinterFormat(PrinterConfig):
    pass


class PrinterPerks(PrinterConfig):
    pass