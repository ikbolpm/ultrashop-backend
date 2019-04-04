from django.db.models import Sum
from rest_framework import serializers
import math

from audio.serializers import AudioSerializer
from brand.serializers import BrandSerializer
from displaySize.serializers import DisplaySerializer
from graphicsCard.serializers import GraphicsSerializer
from laptopType.serializers import LaptopTypeSerializer
from perks.serializers import PerksSerializer
from processor.serializers import ProcessorSerializer
from ram.serializers import RamSerializer
from resolution.serializers import ResolutionSerializer
from settings.models import DollarExchangeRate, TransactionCoefficient
from storage.serializers import StorageSerializer
from .models import Laptop, Image
from inventory.models import Inventory


class ImageSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='fileurl')
    class Meta:
        model = Image
        fields = ('url',)


class LaptopSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    ram_type = RamSerializer()
    processor = ProcessorSerializer()
    main_storage_type = StorageSerializer()
    secondary_storage_type = StorageSerializer()
    screen_size = DisplaySerializer()
    resolution = ResolutionSerializer()
    laptop_type = LaptopTypeSerializer()
    graphics_card = GraphicsSerializer()
    audio = AudioSerializer()
    perks = PerksSerializer(many=True)
    images = ImageSerializer(many=True)

    price_uzs = serializers.SerializerMethodField()
    old_price_uzs = serializers.SerializerMethodField()
    inventory_count = serializers.SerializerMethodField()

    class Meta:
        model = Laptop
        fields = [
            'id',
            'inventory_count',
            'name',
            'slug',
            'brand',
            'model',
            'ram',
            'ram_type',
            'processor',
            'main_storage',
            'main_storage_type',
            'secondary_storage',
            'secondary_storage_type',
            'screen_size',
            'resolution',
            'laptop_type',
            'graphics_card',
            'graphics_card_memory',
            'audio',
            'perks',
            'price',
            'price_uzs',
            'old_price',
            'old_price_uzs',
            'thumbnail',
            'images',
            'created',
            'updated'
        ]

    def get_price_uzs(self, obj):
        return int(math.ceil(obj.price * DollarExchangeRate.objects.filter().first().exchange_rate / TransactionCoefficient.objects.filter().first().coefficient)/1000)*1000

    def get_old_price_uzs(self, obj):
        return int(math.ceil(obj.old_price * DollarExchangeRate.objects.filter().first().exchange_rate / TransactionCoefficient.objects.filter().first().coefficient)/1000)*1000

    def get_inventory_count(self, obj):
        return Inventory.objects.filter(laptop_id__exact=obj).values('laptop').annotate(quantity=Sum('quantity'))

