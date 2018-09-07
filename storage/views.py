from rest_framework import generics

from .models import Storage
from .serializers import StorageSerializer


class StorageListView(generics.ListAPIView):
    serializer_class = StorageSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Storage.objects.all()
