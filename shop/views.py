from django_filters import FilterSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter

from .models import Product, Image, Category
from .pagination import ProductLimitOffsetPagination
from .serializers import ImageSerializer, CategorySerializer, ProductSerializer


class ImageListApiView(generics.ListAPIView):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()


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
    class Meta:
        model = Product
        fields = ('category__slug', 'brand', 'vat')


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