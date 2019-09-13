from django.db.models import Sum
from rest_framework import serializers
import math

from inventory.models import Inventory
from settings.models import DollarExchangeRate, TransactionCoefficient
from .models import Category, Brand, Product, Image


class ImageSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='fileurl')
    class Meta:
        model = Image
        fields = ('url',)


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = [
            'id',
            'name',
            'slug',
            'logo',
            'active',
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'parent',
            'name',
            'name_singular',
            'short_description',
            'slug',
            'logo',
        ]


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()
    price_uzs = serializers.SerializerMethodField()
    old_price_uzs = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id',
            'upc',
            'category',
            'brand',
            'name',
            'slug',
            'model',
            'description',
            'old_price',
            'old_price_uzs',
            'price',
            'price_uzs',
            'viewed',
            'thumbnail',
            'awaiting',
            'vat',
            'created',
            'updated',
        ]

    def get_price_uzs(self, obj):
        return int(math.ceil(obj.price * DollarExchangeRate.objects.filter().first().exchange_rate / TransactionCoefficient.objects.filter().first().coefficient)/10000)*10000

    def get_old_price_uzs(self, obj):
        return int(math.ceil(obj.old_price * DollarExchangeRate.objects.filter().first().exchange_rate / TransactionCoefficient.objects.filter().first().coefficient)/10000)*10000

    def get_inventory_count(self, obj):
        return Inventory.objects.filter(laptop_id__exact=obj).values('laptop').annotate(quantity=Sum('quantity'))