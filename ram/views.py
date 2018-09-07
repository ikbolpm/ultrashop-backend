from rest_framework import generics

from .models import Ram
from .serializers import RamSerializer


class RamListView(generics.ListAPIView):
    serializer_class = RamSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Ram.objects.all()
