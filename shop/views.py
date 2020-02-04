from django.db.models import Sum
from django_filters import FilterSet
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter

from stock.models import Inventory
from .models import Product, Image, Category, Laptop
from .pagination import ProductLimitOffsetPagination
from .serializers import ImageSerializer, CategorySerializer, ProductSerializer, LaptopSerializer


class ImageFilter(FilterSet):
    class Meta:
        model = Image
        fields = ('gallery__slug',)


class ImageListApiView(generics.ListAPIView):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_class = ImageFilter


class CategoryFilter(FilterSet):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'active')


class CategoryListApiView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_class = CategoryFilter
    ordering_fields = (
        'id',
        'name',
    )


class ProductFilter(FilterSet):
    slug_not = filters.CharFilter(field_name='slug', exclude=True)
    quantity = filters.CharFilter(method='filter_by_quantity')

    class Meta:
        model = Product
        fields = ('category__slug', 'brand', 'vat',)

    def filter_by_slug_not(self, queryset, name, value):
        queryset = queryset.filter(self.slug != value)
        return queryset

    def filter_by_quantity(self, queryset, name, value):
        inv_queryset = Inventory.objects.all()\
            .values('product')\
            .annotate(quantity=Sum('quantity'))\
            .filter(quantity__gt=value)\
            .values('product')
        return queryset.filter(id__in=inv_queryset)


class ProductListApiView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_class = ProductFilter
    pagination_class = ProductLimitOffsetPagination
    ordering_fields = (
        'id',
        'name',
        'price',
    )
    search_fields = (
        'upc',
        'name',
        'part_number',
        'slug',
        'description',
    )


class LaptopFilter(FilterSet):
    class Meta:
        model = Laptop
        fields = ('slug', 'category__slug', 'brand', 'vat',)


class LaptopListApiView(generics.ListAPIView):
    serializer_class = LaptopSerializer
    queryset = Laptop.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_class = LaptopFilter
    pagination_class = ProductLimitOffsetPagination
    ordering_fields = (
        'id',
        'name',
        'price',
    )
    search_fields = (
        'upc',
        'name',
        'part_number',
        'slug',
        'description',
    )