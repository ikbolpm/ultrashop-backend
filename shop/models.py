from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField

from audio.models import Audio
from brand.models import Brand
from displaySize.models import DisplaySize
from graphicsCard.models import GraphicsCard
from processor.models import Processor
from ram.models import Ram
from resolution.models import Resolution
from productconfig.models import ComputerPerk, LaptopType, PrinterColorType, PrinterTechnologyType, PrinterFunction, \
    PrinterFormat, AllInOneType, DesktopType, PrinterPerks


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


class Product(models.Model):
    upc = models.CharField(max_length=12, help_text='Отсканируйте баркод',unique=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products_brand')
    name = models.CharField(max_length=255, help_text='К примеру: XPS 13')
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, null=True, unique=True)
    type = models.CharField(max_length=100)
    part_number = models.CharField(max_length=30, help_text='К примеру: 81XVS440S', blank=True, null=True, unique=True)
    old_price = models.IntegerField(help_text='Старая цена. Оставьте 0 если не идет акция', blank=True, null=True)
    price = models.IntegerField(help_text='Введите сумму в USD')
    warranty = models.IntegerField(help_text='Введите срок гарантии в месяцах', default=12)
    viewed = models.IntegerField(default=0)
    thumbnail = models.ImageField(upload_to='images/products/thumbnails')
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
        return "{} / {}".format(self.type, self.title)


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
    laptop_type = models.ManyToManyField(LaptopType)
    processor = models.ForeignKey(Processor, on_delete=models.CASCADE, related_name='laptop_processor')
    ram = models.IntegerField()
    ram_type = models.ForeignKey(Ram, on_delete=models.CASCADE, related_name='laptop_ram_type')
    ssd = models.IntegerField(blank=True, null=True)
    hdd = models.IntegerField(blank=True, null=True)
    optane = models.IntegerField(blank=True, null=True)
    graphics_card = models.ForeignKey(GraphicsCard, on_delete=models.CASCADE, blank=True, null=True,
                                      related_name='laptop_graphics_card')
    graphics_card_memory = models.IntegerField(help_text='В ГГБ. К примеру 2 или 4', blank=True, null=True)
    screen_size = models.ForeignKey(DisplaySize, on_delete=models.CASCADE, related_name='laptop_screen_size')
    resolution = models.ForeignKey(Resolution, on_delete=models.CASCADE, related_name='laptop_resolution')
    audio = models.ForeignKey(Audio, on_delete=models.CASCADE, related_name='laptop_audio')
    perks = models.ManyToManyField(ComputerPerk)

    def save_base(self, raw=False, force_insert=False, force_update=False, using=None, update_fields=None):
        new_creation = False
        if self.part_number:
            part_number = str(self.part_number) + ' / '
        else:
            part_number = ''

        if self.ssd:
            ssd = str(self.ssd) + 'GB SSD / '
        else:
            ssd = ''
        if self.hdd:
            hdd = str(self.hdd) + 'GB HDD / '
        else:
            hdd = ''
        if self.optane:
            optane = str(self.optane) + 'GB Optane / '
        else:
            optane = ''
        if self.graphics_card:
            graphics_card = str(self.graphics_card)
            graphics_memory = ' ' + str(self.graphics_card_memory) + ' GB'
        else:
            graphics_card = str(self.processor.integrated_graphics)
            graphics_memory = ''

        self.title = self.brand.name + ' / ' \
                    + self.name + ' / ' \
                    + part_number \
                    + str(self.screen_size) + ' / '\
                    + str(self.resolution) + ' / '\
                    + self.processor.name + ' / '\
                    + str(self.ram) + 'GB ' + str(self.ram_type) + ' / '\
                    + ssd + hdd + optane \
                    + graphics_card + graphics_memory
        if not self.id:
            new_creation = True
        if new_creation:
            self.slug = slugify(self.title)
        super().save_base(raw, force_insert, force_update, using, update_fields)


class AllInOne(Product):
    all_in_one_type = models.ManyToManyField(AllInOneType)
    processor = models.ForeignKey(Processor, on_delete=models.CASCADE, related_name='aio_processor')
    ram = models.IntegerField()
    ram_type = models.ForeignKey(Ram, on_delete=models.CASCADE, related_name='aio_ram_type')
    ssd = models.IntegerField(blank=True, null=True)
    hdd = models.IntegerField(blank=True, null=True)
    optane = models.IntegerField(blank=True, null=True)
    models.IntegerField(blank=True, null=True)
    graphics_card = models.ForeignKey(GraphicsCard, on_delete=models.CASCADE, blank=True, null=True,
                                      related_name='aio_graphics_card')
    graphics_card_memory = models.IntegerField(help_text='В ГГБ. К примеру 2 или 4', blank=True, null=True)
    screen_size = models.ForeignKey(DisplaySize, on_delete=models.CASCADE, related_name='aio_screen_size')
    resolution = models.ForeignKey(Resolution, on_delete=models.CASCADE, related_name='aio_resolution')
    audio = models.ForeignKey(Audio, on_delete=models.CASCADE, related_name='aio_audio')
    perks = models.ManyToManyField(ComputerPerk)

    def save_base(self, raw=False, force_insert=False, force_update=False, using=None, update_fields=None):
        new_creation = True
        if self.part_number:
            part_number = str(self.part_number) + ' / '
        else:
            part_number = ''

        if self.ssd:
            ssd = str(self.ssd) + 'GB SSD / '
        else:
            ssd = ''
        if self.hdd:
            hdd = str(self.hdd) + 'GB HDD / '
        else:
            hdd = ''
        if self.optane:
            optane = str(self.optane) + 'GB Optane / '
        else:
            optane = ''
        if self.graphics_card:
            graphics_card = str(self.graphics_card)
            graphics_memory = ' ' + str(self.graphics_card_memory) + ' GB'
        else:
            graphics_card = str(self.processor.integrated_graphics)
            graphics_memory = ''

        self.title = self.brand.name + ' / ' \
                    + self.name + ' / ' \
                    + part_number \
                    + str(self.screen_size) + ' / '\
                    + str(self.resolution) + ' / '\
                    + self.processor.name + ' / '\
                    + str(self.ram) + 'GB ' + str(self.ram_type) + ' / '\
                    + ssd + hdd + optane \
                    + graphics_card + graphics_memory
        if not self.id:
            new_creation = True
        if new_creation:
            self.slug = slugify(self.title)
        super().save_base(raw, force_insert, force_update, using, update_fields)


class Desktop(Product):
    desktop_type = models.ManyToManyField(DesktopType)
    processor = models.ForeignKey(Processor, on_delete=models.CASCADE, related_name='desktop_processor')
    ram = models.IntegerField()
    ram_type = models.ForeignKey(Ram, on_delete=models.CASCADE, related_name='desktop_ram_type')
    ssd = models.IntegerField(blank=True, null=True)
    hdd = models.IntegerField(blank=True, null=True)
    optane = models.IntegerField(blank=True, null=True)
    models.IntegerField(blank=True, null=True)
    graphics_card = models.ForeignKey(GraphicsCard, on_delete=models.CASCADE, blank=True, null=True,
                                      related_name='desktop_graphics_card')
    graphics_card_memory = models.IntegerField(help_text='В ГГБ. К примеру 2 или 4', blank=True, null=True)
    screen_size = models.ForeignKey(DisplaySize, on_delete=models.CASCADE, related_name='desktop_screen_size', null=True, blank=True)
    resolution = models.ForeignKey(Resolution, on_delete=models.CASCADE, related_name='desktop_resolution', null=True, blank=True)
    perks = models.ManyToManyField(ComputerPerk)

    def save_base(self, raw=False, force_insert=False, force_update=False, using=None, update_fields=None):
        new_creation = False
        if self.part_number:
            part_number = str(self.part_number) + ' / '
        else:
            part_number = ''

        if self.ssd:
            ssd = str(self.ssd) + 'GB SSD / '
        else:
            ssd = ''
        if self.hdd:
            hdd = str(self.hdd) + 'GB HDD / '
        else:
            hdd = ''
        if self.optane:
            optane = str(self.optane) + 'GB Optane / '
        else:
            optane = ''
        if self.graphics_card:
            graphics_card = str(self.graphics_card)
            graphics_memory = ' ' + str(self.graphics_card_memory) + ' GB'
        else:
            graphics_card = str(self.processor.integrated_graphics)
            graphics_memory = ''
        if self.screen_size:
            screen_size = str(self.screen_size) + '" / '
        else:
            screen_size = ' NO LCD / '
        if self.resolution:
            resolution = str(self.screen_size) + '" / '
        else:
            resolution = ''

        self.title = self.brand.name + ' / ' \
                    + self.name + ' / ' \
                    + part_number \
                    + screen_size + resolution \
                    + self.processor.name + ' / '\
                    + str(self.ram) + 'GB ' + str(self.ram_type) + ' / '\
                    + ssd + hdd + optane \
                    + graphics_card + graphics_memory
        if not self.id:
            new_creation = True
        if new_creation:
            self.slug = slugify(self.title)
        super().save_base(raw, force_insert, force_update, using, update_fields)


class Printer(Product):
    color = models.ForeignKey(PrinterColorType, on_delete=models.CASCADE)
    technology = models.ForeignKey(PrinterTechnologyType, on_delete=models.CASCADE)
    functions = models.ManyToManyField(PrinterFunction)
    formats = models.ManyToManyField(PrinterFormat)
    speed = models.PositiveIntegerField(help_text='скорость печати за 1 минуту')
    perks = models.ManyToManyField(PrinterPerks)
    description = HTMLField(blank=True, null=True)

    def save_base(self, raw=False, force_insert=False, force_update=False, using=None, update_fields=None):
        new_creation = False
        if self.part_number:
            part_number = str(self.part_number) + ' / '
        else:
            part_number = ''
        formats = ''
        for format in self.formats.all():
            formats += str(format) + '-'
        formats = formats[:-1]
        functions = ''
        for function in self.functions.all():
            functions += str(function) + '-'
        functions = functions[:-1]
        self.title = self.brand.name + ' / ' \
                    + self.name + ' / ' \
                    + part_number \
                    + self.color.name + ' / '\
                    + self.technology.name + ' / '\
                    + functions + ' / '\
                    + formats + ' / ' \
                    + str(self.speed) + ' стр в мин /'\
                    + str(self.warranty) + ' месяцев гарантии'
        if not self.id:
            new_creation = True
        if new_creation:
            self.slug = slugify(self.title)
        super().save_base(raw, force_insert, force_update, using, update_fields)
