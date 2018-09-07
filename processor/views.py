from rest_framework import generics

from .models import Processor
from .serializers import ProcessorSerializer


class ProcessorListView(generics.ListAPIView):
    serializer_class = ProcessorSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Processor.objects.all()
