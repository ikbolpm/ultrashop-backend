from rest_framework import generics

from .models import DisplaySize
from .serializers import DisplaySerializer


class DisplayListView(generics.ListAPIView):
    serializer_class = DisplaySerializer
    lookup_field = 'id'

    def get_queryset(self):
        return DisplaySize.objects.all()
