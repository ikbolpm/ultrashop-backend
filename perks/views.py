from rest_framework import generics

from .models import Perks
from .serializers import PerksSerializer


class PerksListView(generics.ListAPIView):
    serializer_class = PerksSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Perks.objects.all()
