from django.db import models
from django.urls import reverse

from audio.models import Audio
from brand.models import Brand
from displaySize.models import DisplaySize
from graphicsCard.models import GraphicsCard
from processor.models import Processor
from ram.models import Ram
from resolution.models import Resolution


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    logo = models.ImageField(upload_to='images/products/categories')
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])


class Product(models.Model):
    upc = models.CharField(max_length=12, help_text='Отсканируйте баркод',unique=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products_brand')
    name = models.CharField(max_length=255, help_text='К примеру: XPS 13')
    slug = models.SlugField(max_length=255)
    type = models.CharField(max_length=100)
    # model = models.CharField(max_length=255, help_text='К примеру: 1470 80XA')
    part_number = models.CharField(max_length=30, help_text='К примеру: 81XVS440S', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    old_price = models.IntegerField(help_text='Старая цена. Оставьте 0 если не идет акция', default=0)
    price = models.IntegerField(help_text='Введите сумму в USD')
    viewed = models.IntegerField(default=0)
    thumbnail = models.ImageField(upload_to='images/products/thumbnails', blank=True, null=True)
    awaiting = models.BooleanField(default=False)
    vat = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        index_together = (('id', 'slug'),)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.type = self.__class__.__name__
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return "{} / {}".format(self.type, self.name)

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])

class Image(models.Model):
    file = models.FileField(upload_to='images/products/productimages/%Y-%m-%d/')
    gallery = models.ForeignKey('Product', related_name='product_images', on_delete=models.CASCADE, blank=True,
                                null=True)

    def __str__(self):
        return self.filename

    @property
    def filename(self):
        return self.file.name.rsplit('/', 1)[-1]

    @property
    def fileurl(self):
        return self.file.url


class Laptop(Product):
    processor = models.ForeignKey(Processor, on_delete=models.CASCADE, related_name='laptop_processor')
    ram = models.IntegerField()
    ram_type = models.ForeignKey(Ram, on_delete=models.CASCADE, related_name='laptop_ram_type')
    ssd = models.IntegerField(blank=True, null=True)
    hdd = models.IntegerField(blank=True, null=True)
    graphics_card = models.ForeignKey(GraphicsCard, on_delete=models.CASCADE, blank=True, null=True,
                                      related_name='laptop_graphics_card')
    graphics_card_memory = models.IntegerField(help_text='В ГГБ. К примеру 2 или 4', blank=True, null=True)
    screen_size = models.ForeignKey(DisplaySize, on_delete=models.CASCADE, related_name='laptop_screen_size')
    resolution = models.ForeignKey(Resolution, on_delete=models.CASCADE, related_name='laptop_resolution')
    # screen_perks = models.ManyToManyField(ScreenPerk, related_name='laptop_screen_perks')
    audio = models.ForeignKey(Audio, on_delete=models.CASCADE, related_name='laptop_audio')


class AllInOne(Product):
    processor = models.ForeignKey(Processor, on_delete=models.CASCADE, related_name='aio_processor')
    ram = models.IntegerField()
    ram_type = models.ForeignKey(Ram, on_delete=models.CASCADE, related_name='aio_ram_type')
    ssd = models.IntegerField(blank=True, null=True)
    hdd = models.IntegerField(blank=True, null=True)
    graphics_card = models.ForeignKey(GraphicsCard, on_delete=models.CASCADE, blank=True, null=True,
                                      related_name='aio_graphics_card')
    graphics_card_memory = models.IntegerField(help_text='В ГГБ. К примеру 2 или 4', blank=True, null=True)
    screen_size = models.ForeignKey(DisplaySize, on_delete=models.CASCADE, related_name='aio_screen_size')
    resolution = models.ForeignKey(Resolution, on_delete=models.CASCADE, related_name='aio_resolution')
    # screen_perks = models.ManyToManyField(ScreenPerk, related_name='laptop_screen_perks')
    audio = models.ForeignKey(Audio, on_delete=models.CASCADE, related_name='aio_audio')