from django.db import models
from django.conf import settings

from audio.models import Audio
from brand.models import Brand
from displaySize.models import DisplaySize
from graphicsCard.models import GraphicsCard
from laptopType.models import LaptopType
from perks.models import Perks
from processor.models import Processor
from ram.models import Ram
from resolution.models import Resolution
from storage.models import Storage



class Laptop(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand')
    name = models.CharField(max_length=255, help_text='К примеру: XPS 13')
    slug = models.SlugField(max_length=255)
    model = models.CharField(max_length=255, help_text='К примеру: 1470 80XA', null=True, blank=True)
    ram = models.IntegerField()
    ram_type = models.ForeignKey(Ram, on_delete=models.CASCADE, related_name='ram_type')
    processor = models.ForeignKey(Processor, on_delete=models.CASCADE, )
    main_storage = models.IntegerField()
    main_storage_type = models.ForeignKey(Storage, on_delete=models.CASCADE, related_name='main_storage', )
    secondary_storage = models.IntegerField(blank=True, null=True)
    secondary_storage_type = models.ForeignKey(Storage, on_delete=models.CASCADE, related_name='secondary_storage',
                                               blank=True, null=True)
    screen_size = models.ForeignKey(DisplaySize, on_delete=models.CASCADE, )
    resolution = models.ForeignKey(Resolution, on_delete=models.CASCADE, )
    laptop_type = models.ForeignKey(LaptopType, on_delete=models.CASCADE, )
    graphics_card = models.ForeignKey(GraphicsCard, on_delete=models.CASCADE, blank=True, null=True)
    graphics_card_memory = models.IntegerField(help_text='В ГГБ. К примеру 2 или 4', blank=True, null=True)
    audio = models.ForeignKey(Audio, on_delete=models.CASCADE, )
    perks = models.ManyToManyField(Perks, help_text='Выберите все нужные опции нажатием кнопки CTRL', blank=True)
    price = models.IntegerField(help_text='Введите сумму в USD')
    viewed = models.IntegerField(default=0,blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        if self.model:
            return self.brand.name + ' ' + self.name + ' ' + self.model
        else:
            return self.brand.name + ' ' + self.name

class Image(models.Model):
    file = models.FileField(upload_to='laptop_images/%Y-%m-%d/')
    gallery = models.ForeignKey(Laptop, related_name='images', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.filename

    @property
    def filename(self):
        return self.file.name.rsplit('/', 1)[-1]

    @property
    def fileurl(self):
        return self.file.url
