from rest_framework import generics

from .models import ProcessorBrand
from .serializers import ProcessorBrandSerializer


class ProcessorBrandListView(generics.ListAPIView):
    serializer_class = ProcessorBrandSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return ProcessorBrand.objects.all()
