from django_filters import FilterSet
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter

from brand.models import Brand
from .pagination import ProductLimitOffsetPagination
from .models import Category, Product, Image
from .serializers import CategorySerializer, ImageSerializer, ProductSerializer
from .models import Perks
from .serializers import PerksSerializer


class CategoryFilter(FilterSet):
    class Meta:
        model = Category
        fields = ('name', 'slug', 'id', 'active')

class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_class = CategoryFilter


    def get_queryset(self):
        return Category.objects.all().order_by('id')


class ProductFilter (FilterSet):
    id_not = filters.NumberFilter(field_name='id',exclude=True)
    brand = filters.CharFilter(method='filter_by_brand')
    category = filters.CharFilter(method='filter_by_category')
    perks = filters.CharFilter(method='filter_by_perks')
    old_price = filters.CharFilter(method='filter_by_old_price')
    # quantity = filters.CharFilter(method='filter_by_quantity')
    awaiting = filters.CharFilter(method='filter_by_awaiting')

    class Meta:
        model = Product
        fields = (
            'id',
            'slug',

        )

    def filter_by_id_not(self, queryset, name, value):
        queryset = queryset.filter(id != value)
        return queryset
    def filter_by_awaiting(self, queryset, name, value):
        queryset = queryset.filter(awaiting = value)
        return queryset
    def filter_by_old_price(self, queryset, name, value):
        queryset = queryset.filter(old_price__gt=value)
        return queryset
    def filter_by_brand(self, queryset, name, value):
        brand = value.strip().split(',')
        brands = Brand.objects.filter(id__in=brand)
        return queryset.filter(brand__in=brands)
    def filter_by_category(self, queryset, name, value):
        category = value.strip().split(',')
        categories = Category.objects.filter(id__in=category)
        return queryset.filter(category__in=categories)
    def filter_by_perks(self, queryset, name, value):
        perks = value.strip().split(',')
        perk = Perks.objects.filter(slug__in=perks)
        return queryset.filter(perks__in=perk)

class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_class = ProductFilter
    pagination_class = ProductLimitOffsetPagination
    # pagination_class = LaptopPageNumberPagination

    ordering_fields = (
        'price',
        'updated'
    )


    search_fields = (
        # 'brand',
        # 'perks',
        'name',
        # 'category',
        'description',
        'slug',
    )

class ProductImagesView(generics.ListAPIView):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
    lookup_field = 'images'

    class Meta:
        model = Image,
        fields = [
            'file.url',
        ]

class PerksListView(generics.ListAPIView):
    serializer_class = PerksSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Perks.objects.all()