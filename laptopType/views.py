from rest_framework import generics

from .models import LaptopType
from .serializers import LaptopTypeSerializer


class LaptopTypeListView(generics.ListAPIView):
    serializer_class = LaptopTypeSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return LaptopType.objects.all().order_by('id')
