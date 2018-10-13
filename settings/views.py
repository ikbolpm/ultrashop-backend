from rest_framework import generics

from .models import DollarExchangeRate
from .serializers import DollarExchangeRateSerializer

class DollarExchangeRateListView(generics.ListAPIView):
    serializer_class = DollarExchangeRateSerializer

    def get_queryset(self):
        return DollarExchangeRate.objects.all()