from django.db.models import Sum
from django_filters import FilterSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from .models import Inventory
from .serializers import InventorySerializer


class InventoryFilter(FilterSet):
    class Meta:
        model = Inventory
        fields = ('laptop',)

class InventoryListView(generics.ListAPIView):
    serializer_class = InventorySerializer
    queryset = Inventory.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_class = InventoryFilter



    def get_queryset(self):
        return Inventory.objects.filter(warehouse_id__lt= 8).values('laptop').annotate(quantity = Sum('quantity'))

    # def get_queryset(self):
    #     return Inventory.objects.all().values('laptop').annotate(quantity = Sum('quantity'))