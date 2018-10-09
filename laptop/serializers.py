from rest_framework import serializers

from audio.serializers import AudioSerializer
from brand.serializers import BrandSerializer
from displaySize.serializers import DisplaySerializer
from graphicsCard.serializers import GraphicsSerializer
from laptopType.serializers import LaptopTypeSerializer
from perks.serializers import PerksSerializer
from processor.serializers import ProcessorSerializer
from ram.serializers import RamSerializer
from resolution.serializers import ResolutionSerializer
from storage.serializers import StorageSerializer
from .models import Laptop, Image


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
    class Meta:
        model = Laptop
        fields = [
            'id',
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
            'images',
            'created',
            'updated'
        ]