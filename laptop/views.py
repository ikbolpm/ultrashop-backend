from django_filters import FilterSet
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter

from audio.models import Audio
from brand.models import Brand
from graphicsCard.models import GraphicsCard
from laptopType.models import LaptopType
from perks.models import Perks
from processor.models import Processor
from processorBrand.models import ProcessorBrand
from ram.models import Ram
from resolution.models import Resolution
from .models import Laptop, Image
from .pagination import LaptopPageNumberPagination, LaptopLimitOffsetPagination
from .serializers import LaptopSerializer, ImageSerializer


class LaptopFilter (FilterSet):
    min_price = filters.CharFilter(method='filter_by_min_price')
    max_price = filters.CharFilter(method='filter_by_max_price')
    min_ram = filters.CharFilter(method='filter_by_min_ram')
    max_ram = filters.CharFilter(method='filter_by_max_ram')
    min_storage = filters.CharFilter(method='filter_by_min_storage')
    max_storage = filters.CharFilter(method='filter_by_max_storage')
    min_cores = filters.CharFilter(method='filter_by_min_cores')
    max_cores = filters.CharFilter(method='filter_by_max_cores')
    min_threads= filters.CharFilter(method='filter_by_min_threads')
    max_threads = filters.CharFilter(method='filter_by_max_threads')
    min_graphics = filters.CharFilter(method='filter_by_min_graphics')
    max_graphics = filters.CharFilter(method='filter_by_max_graphics')
    min_size = filters.CharFilter(method='filter_by_min_size')
    max_size = filters.CharFilter(method='filter_by_max_size')
    ram = filters.CharFilter(method='filter_by_ram')
    brand = filters.CharFilter(method='filter_by_brand')
    processor = filters.CharFilter(method='filter_by_processor')
    processor_brand = filters.CharFilter(method='filter_by_processor_brand')
    storage = filters.CharFilter(method='filter_by_storage')
    resolution = filters.CharFilter(method='filter_by_resolution')
    type = filters.CharFilter(method='filter_by_type')
    graphics = filters.CharFilter(method='filter_by_graphics')
    audio = filters.CharFilter(method='filter_by_audio')
    perks = filters.CharFilter(method='filter_by_perks')
    # size = filters.CharFilter(method='filter_by_size')


    class Meta:
        model = Laptop
        fields = (
            'id',
            'slug'
        )

    def filter_by_min_price(self, queryset, name, value):
        queryset = queryset.filter(price__gte=value)
        return queryset
    def filter_by_max_price(self, queryset, name, value):
        queryset = queryset.filter(price__lte=value)
        return queryset
    def filter_by_min_ram(self, queryset, name, value):
        queryset = queryset.filter(ram__gte=value)
        return queryset
    def filter_by_max_ram(self, queryset, name, value):
        queryset = queryset.filter(ram__lte=value)
        return queryset
    def filter_by_min_storage(self, queryset, name, value):
        queryset = queryset.filter(main_storage__gte=value)
        return queryset
    def filter_by_max_storage(self, queryset, name, value):
        queryset = queryset.filter(main_storage__lte=value)
        return queryset
    def filter_by_min_cores(self, queryset, name, value):
        queryset = queryset.filter(processor__cores__gte=value)
        return queryset
    def filter_by_max_cores(self, queryset, name, value):
        queryset = queryset.filter(processor__cores__lte=value)
        return queryset
    def filter_by_min_threads(self, queryset, name, value):
        queryset = queryset.filter(processor__threads__gte=value)
        return queryset
    def filter_by_max_threads(self, queryset, name, value):
        queryset = queryset.filter(processor__threads__lte=value)
        return queryset
    def filter_by_min_graphics(self, queryset, name, value):
        queryset = queryset.filter(graphics_card_memory__gte=value)
        return queryset
    def filter_by_max_graphics(self, queryset, name, value):
        queryset = queryset.filter(graphics_card_memory__lte=value)
        return queryset

    def filter_by_min_size(self, queryset, name, value):
        queryset = queryset.filter(screen_size__size__gte=value)
        return queryset
    def filter_by_max_size(self, queryset, name, value):
        queryset = queryset.filter(screen_size__size__lte=value)
        return queryset

    def filter_by_ram(self, queryset, name, value):
        ram_type = value.strip().split(',')
        rams_type__id = Ram.objects.filter(id__in=ram_type)
        return queryset.filter(ram_type__in=rams_type__id)

    def filter_by_brand(self, queryset, name, value):
        brand = value.strip().split(',')
        brands = Brand.objects.filter(id__in=brand)
        return queryset.filter(brand__in=brands)

    def filter_by_processor(self, queryset, name, value):
        processor = value.strip().split(',')
        processors = Processor.objects.filter(id__in=processor)
        return queryset.filter(processor__in=processors)

    def filter_by_processor_brand(self, queryset, name, value):
        processor__brand = value.strip().split(',')
        processors = ProcessorBrand.objects.filter(id__in=processor__brand)
        return queryset.filter(processor__brand__in=processors)

    def filter_by_resolution(self, queryset, name, value):
        resolution = value.strip().split(',')
        resolutions = Resolution.objects.filter(id__in=resolution)
        return queryset.filter(resolution__in=resolutions)

    def filter_by_type(self, queryset, name, value):
        laptop_type = value.strip().split(',')
        laptop_types = LaptopType.objects.filter(id__in=laptop_type)
        return queryset.filter(laptop_type__in=laptop_types)

    def filter_by_graphics(self, queryset, name, value):
        graphics_card = value.strip().split(',')
        graphics_cards = GraphicsCard.objects.filter(id__in=graphics_card)
        return queryset.filter(graphics_card__in=graphics_cards)

    def filter_by_audio(self, queryset, name, value):
        audio = value.strip().split(',')
        audios = Audio.objects.filter(id__in=audio)
        return queryset.filter(audio__in=audios)

    def filter_by_perks(self, queryset, name, value):
        perks = value.strip().split(',')
        perk = Perks.objects.filter(id__in=perks)
        return queryset.filter(perks__in=perk)



class LaptopListView(generics.ListAPIView):
    serializer_class = LaptopSerializer
    queryset = Laptop.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_class = LaptopFilter
    pagination_class = LaptopLimitOffsetPagination
    # pagination_class = LaptopPageNumberPagination


    ordering_fields = (
        'ram',
        'brand__slug',
        'processor__slug',
        'processor__min_frequency',
        'processor__max_frequency',
        'processor__cores',
        'Processor__threads',
        'processor__cache',
        'graphics_card_memory',
        'price',
        'screen_size'
    )
    search_fields = (
        'ram_type__slug',
        'brand__slug',
        'processor__slug',
        'processor__brand__slug',
        'processor__integrated_graphics',
        'main_storage_type__slug',
        'secondary_storage_type__slug',
        'resolution__slug',
        'laptop_type__slug',
        'graphics_card__slug',
        'audio__slug',
        'perks__slug',
        'screen_size__size',
        'name'
    )

class LaptopImagesView(generics.ListAPIView):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
    lookup_field = 'images'

    class Meta:
        model = Image,
        fields = [
            'file.url',
        ]
