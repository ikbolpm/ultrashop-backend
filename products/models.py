from django.db import models
from tinymce.models import HTMLField

from brand.models import Brand


class Category(models.Model):
    name = models.CharField(max_length=200,
                            help_text='Во множественном числе. К примеру: УльтрабукИ, трансформеры и т.д.')
    slug = models.SlugField(max_length=200)
    name_singular = models.CharField(max_length=200,
                                     help_text='В единственном числе. К примеру: Ультрабук, трансформер и т.д.')
    short_description = models.TextField(default="Ultrabuki")
    logo = models.ImageField(upload_to='categories', default='default.png')
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    upc   = models.CharField(max_length=12, help_text='Отсканируйте баркод', default=1)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='product_brand')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='product_category')
    name = models.CharField(max_length=255, help_text='К примеру: XPS 13')
    slug = models.SlugField(max_length=255)
    model = models.CharField(max_length=255, help_text='К примеру: 1470 80XA', null=True, blank=True)
    description = HTMLField(blank=True, null=True)
    perks = models.ManyToManyField('Perks', help_text='Выберите все нужные опции нажатием кнопки CTRL')
    old_price = models.IntegerField(help_text='Старая цена. Оставьте 0 если не идет акция', default=0)
    price = models.IntegerField(help_text='Введите сумму в USD')
    viewed = models.IntegerField(default=0, blank=True, null=True)
    thumbnail = models.ImageField(upload_to='laptop_thumbnails', blank=True, null=True)
    available = models.BooleanField(default=True)
    awaiting = models.BooleanField(default=False)
    vat = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name

    def _is_vat(self):
        if self.vat == True:
            return "NDS"


class Image(models.Model):
    file = models.FileField(upload_to='product_images/%Y-%m-%d/')
    gallery = models.ForeignKey('Product', related_name='images', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.filename

    @property
    def filename(self):
        return self.file.name.rsplit('/', 1)[-1]

    @property
    def fileurl(self):
        return self.file.url

from django.db import models


class Perks(models.Model):
    name = models.CharField(max_length=200, help_text='К примеру: Сенсорный экран')
    slug = models.SlugField(max_length=200)

    class Meta:
        verbose_name = 'Perks'
        verbose_name_plural = 'Perks'
        ordering = ['name']

    def __str__(self):
        return self.name