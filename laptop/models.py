from django.db import models
from PIL import Image
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
    processor = models.ForeignKey(Processor, on_delete=models.CASCADE, )
    ram = models.IntegerField()
    ram_type = models.ForeignKey(Ram, on_delete=models.CASCADE, related_name='ram_type')
    main_storage = models.IntegerField()
    main_storage_type = models.ForeignKey(Storage, on_delete=models.CASCADE, related_name='main_storage', )
    secondary_storage = models.IntegerField(blank=True, null=True)
    secondary_storage_type = models.ForeignKey(Storage, on_delete=models.CASCADE, related_name='secondary_storage',
                                               blank=True, null=True)
    graphics_card = models.ForeignKey(GraphicsCard, on_delete=models.CASCADE, blank=True, null=True)
    graphics_card_memory = models.IntegerField(help_text='В ГГБ. К примеру 2 или 4', blank=True, null=True)
    screen_size = models.ForeignKey(DisplaySize, on_delete=models.CASCADE, )
    resolution = models.ForeignKey(Resolution, on_delete=models.CASCADE, )
    laptop_type = models.ForeignKey(LaptopType, on_delete=models.CASCADE, )
    audio = models.ForeignKey(Audio, on_delete=models.CASCADE, )
    perks = models.ManyToManyField(Perks, help_text='Выберите все нужные опции нажатием кнопки CTRL', blank=True)
    old_price = models.IntegerField(help_text='Старая цена. Оставьте 0 если не идет акция', default=0)
    price = models.IntegerField(help_text='Введите сумму в USD')
    viewed = models.IntegerField(default=0,blank=True, null=True)
    thumbnail = models.ImageField(upload_to='laptop_thumbnails', blank=True, null=True)
    awaiting = models.BooleanField(default=False)
    vat = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        main_storage = str(self.main_storage) + 'GB ' + str(self.main_storage_type)

        if self.model:
            model = ' / ' + str(self.model)
        else:
            model = ' / '

        if self.secondary_storage:
            secondary_storage = ' + ' + str(self.secondary_storage) + ' GB ' + str(self.secondary_storage_type)
        else:
            secondary_storage = ''

        if self.graphics_card:
            graphics_card = ' / ' + str(self.graphics_card)
            graphics_memory = ' ' + str(self.graphics_card_memory) + ' GB'
        else:
            graphics_card = ' / No VGA'
            graphics_memory = ''

        full_name = str(self.brand.name) + ' / ' \
                    + str(self.name) \
                    + model + ' / ' \
                    + str(self.screen_size) + '" ' + str(self.resolution) + ' / ' \
                    + str(self.processor.name) + ' / ' \
                    + str(self.ram) + 'GB ' + str(self.ram_type) + ' / ' \
                    + main_storage \
                    + secondary_storage \
                    + graphics_card + graphics_memory
        return full_name

    def _is_vat(self):
        if self.vat == True:
            return "NDS"

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