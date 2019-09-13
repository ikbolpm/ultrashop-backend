from django_filters import FilterSet
from django_filters import rest_framework as filters
from django.db.models import Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import get_object_or_404

from .models import Category, Brand, Product
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer
from .pagination import ProductLimitOffsetPagination


class CategoryFilter(FilterSet):
    level = filters.NumberFilter(field_name='level', exclude=False)
    class Meta:
        model = Category
        fields = ('parent', 'name', 'slug', 'id',)

class CategoryListAPIView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_class = CategoryFilter


    def get_queryset(self):
        return Category.objects.all().order_by('id')


class BrandFilter(FilterSet):
    class Meta:
        model = Brand
        fields = ('name', 'slug', 'active')

class BrandListAPIView(generics.ListAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_class = BrandFilter

    def get_queryset(self):
        return Brand.objects.all().order_by('name')


class ProductFilter(FilterSet):
    id_not = filters.NumberFilter(field_name='id', exclude=True)
    category = filters.CharFilter(method='filter_by_category')

    class Meta:
        model = Product
        fields = (
            'id',
            'slug',
            'category',
            'brand',
            'vat',
        )

    def filter_by_category(self, queryset, value, name):
        categories = Category.objects.all()
        category = get_object_or_404(categories, id=name)
        categories = category.get_descendants(include_self=True)
        return queryset.filter(category__in=categories)


class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_class = ProductFilter
    pagination_class = ProductLimitOffsetPagination


