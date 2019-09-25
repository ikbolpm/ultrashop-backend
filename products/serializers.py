import math
from rest_framework import serializers

from brand.serializers import BrandSerializer
from settings.models import DollarExchangeRate, TransactionCoefficient
from .models import Category, Image, Product, Perks


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'slug',
            'name_singular',
            'logo',
            'short_description',
            'active'
        ]


class ImageSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='fileurl')
    class Meta:
        model = Image
        fields = ('url',)


class PerksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perks
        fields = [
            'id',
            'name',
            'slug'
        ]


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()
    images = ImageSerializer(many=True)
    price_uzs = serializers.SerializerMethodField()
    old_price_uzs = serializers.SerializerMethodField()
    perks = PerksSerializer(many=True)
    # inventory_count = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id',
            # 'inventory_count',
            'available',
            'name',
            'slug',
            'brand',
            'category',
            'model',
            'perks',
            'price',
            'price_uzs',
            'old_price',
            'old_price_uzs',
            'thumbnail',
            'images',
            # 'awaiting',
            'vat',
            # 'short_description',
            'created',
            'updated',
            'description'
        ]

    def get_price_uzs(self, obj):
        return int(math.ceil(obj.price * DollarExchangeRate.objects.filter().first().exchange_rate / TransactionCoefficient.objects.filter().first().coefficient)/1000)*1000

    def get_old_price_uzs(self, obj):
        return int(math.ceil(obj.old_price * DollarExchangeRate.objects.filter().first().exchange_rate / TransactionCoefficient.objects.filter().first().coefficient)/1000)*1000

    # def get_inventory_count(self, obj):
    #     return ProductInventory.objects.filter(product_id__exact=obj).values('product').annotate(quantity=Sum('quantity'))
