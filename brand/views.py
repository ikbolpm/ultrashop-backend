from django_filters import FilterSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from .models import Brand
from .serializers import BrandSerializer


class BrandFilter(FilterSet):
    class Meta:
        model = Brand
        fields = ('name', 'slug', 'active')

class BrandListView(generics.ListAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_class = BrandFilter

    def get_queryset(self):
        return Brand.objects.all()