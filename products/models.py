from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from tinymce.models import HTMLField

from brand.models import Brand


class Category(MPTTModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    name = models.CharField(max_length=200,
                            help_text='Во множественном числе. К примеру: УльтрабукИ, трансформеры и т.д.')
    slug = models.SlugField(max_length=200)
    name_singular = models.CharField(max_length=200,
                                     help_text='В единственном числе. К примеру: Ультрабук, трансформер и т.д.')
    short_description = models.TextField()
    logo = models.ImageField(upload_to='category/thumbs', default='default.png')

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=200, help_text='К примеру: Asus, Acer, HP и т.д.')
    slug = models.SlugField(max_length=200)
    logo = models.ImageField(upload_to='brands')
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    upc = models.CharField(max_length=12, help_text='Отсканируйте баркод', unique=True)
    category = TreeForeignKey('Category', on_delete=models.CASCADE)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, related_name='brand')
    name = models.CharField(max_length=255, help_text='К примеру: XPS 13')
    slug = models.SlugField(max_length=255)
    model = models.CharField(max_length=255, help_text='К примеру: 1470 80XA')
    description = HTMLField()
    old_price = models.IntegerField(help_text='Старая цена. Оставьте 0 если не идет акция', default=0)
    price = models.IntegerField(help_text='Введите сумму в USD')
    viewed = models.IntegerField(default=0, blank=True, null=True)
    thumbnail = models.ImageField(upload_to='products/thumbnails', blank=True, null=True)
    awaiting = models.BooleanField(default=False)
    vat = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return "{} / {}".format(self.name, self.model)

    def _is_vat(self):
        if self.vat == True:
            return "NDS"


class Image(models.Model):
    file = models.FileField(upload_to='product/images/%Y-%m-%d/')
    gallery = models.ForeignKey('Product', related_name='images', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.filename

    @property
    def filename(self):
        return self.file.name.rsplit('/', 1)[-1]

    @property
    def fileurl(self):
        return self.file.url