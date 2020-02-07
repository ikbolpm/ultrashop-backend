from django.db.models import Sum
from rest_framework import serializers
import math

from audio.serializers import AudioSerializer
from displaySize.serializers import DisplaySerializer
from graphicsCard.serializers import GraphicsSerializer
from processor.serializers import ProcessorSerializer
from ram.serializers import RamSerializer
from resolution.serializers import ResolutionSerializer
from sitesettings.models import DollarExchangeRate, TransactionCoefficient
from stock.models import Inventory
from .models import Category, Product, Image, Laptop, AllInOne, Desktop
from brand.serializers import BrandSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'slug',
            'active',
            'logo'
        ]


class ImageSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='fileurl')

    class Meta:
        model = Image
        fields = ('url',)


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()
    price_uzs = serializers.SerializerMethodField()
    old_price_uzs = serializers.SerializerMethodField()
    inventory_count = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'title',
            'slug',
            'category',
            'thumbnail',
            'brand',
            'price',
            'old_price',
            'price_uzs',
            'old_price_uzs',
            'inventory_count',
        ]

    def get_price_uzs(self, obj):
        return int(math.ceil(obj.price * DollarExchangeRate.objects.filter().first().exchange_rate / TransactionCoefficient.objects.filter().first().coefficient)/1000)*1000

    def get_old_price_uzs(self, obj):
        if obj.old_price:
            return int(math.ceil(obj.old_price * DollarExchangeRate.objects.filter().first().exchange_rate / TransactionCoefficient.objects.filter().first().coefficient)/1000)*1000

    def get_inventory_count(self, obj):
        return Inventory.objects.filter(product_id__exact=obj).values('product').annotate(quantity=Sum('quantity'))


class LaptopSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()
    ram_type = RamSerializer()
    processor = ProcessorSerializer()
    screen_size = DisplaySerializer()
    resolution = ResolutionSerializer()
    graphics_card = GraphicsSerializer()
    audio = AudioSerializer()
    price_uzs = serializers.SerializerMethodField()
    old_price_uzs = serializers.SerializerMethodField()
    inventory_count = serializers.SerializerMethodField()

    class Meta:
        model = Laptop
        fields = [
            'id',
            'name',
            'slug',
            'category',
            'thumbnail',
            'brand',
            'price',
            'old_price',
            'price_uzs',
            'old_price_uzs',
            'inventory_count',
            'processor',
            'ram',
            'ram_type',
            'screen_size',
            'graphics_card',
            'graphics_card_memory',
            'resolution',
            'ssd',
            'hdd',
            'optane',
            'audio',
            'warranty',
            'vat',
            'part_number'
        ]

    def get_price_uzs(self, obj):
        return int(math.ceil(
            obj.price * DollarExchangeRate.objects.filter().first().exchange_rate / TransactionCoefficient.objects.filter().first().coefficient) / 1000) * 1000

    def get_old_price_uzs(self, obj):
        if obj.old_price:
            return int(math.ceil(
                obj.old_price * DollarExchangeRate.objects.filter().first().exchange_rate / TransactionCoefficient.objects.filter().first().coefficient) / 1000) * 1000

    def get_inventory_count(self, obj):
        return Inventory.objects.filter(product_id__exact=obj).values('product').annotate(quantity=Sum('quantity'))