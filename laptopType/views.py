from django_filters import FilterSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from .models import LaptopType
from .serializers import LaptopTypeSerializer

class LaptopTypeFilter(FilterSet):
    class Meta:
        model = LaptopType
        fields = ('name', 'slug', 'id',)

class LaptopTypeListView(generics.ListAPIView):
    serializer_class = LaptopTypeSerializer
    queryset = LaptopType.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_class = LaptopTypeFilter


    def get_queryset(self):
        return LaptopType.objects.all().order_by('id')