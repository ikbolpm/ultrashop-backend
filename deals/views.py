from django_filters import FilterSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .models import Deal
from .serializers import DealSerializer


class DealFilter(FilterSet):
    class Meta:
        model = Deal
        fields = ('active',)


class DealListView(generics.ListAPIView):
    serializer_class = DealSerializer
    queryset = Deal.objects.all()
    filter_backends = (DjangoFilterBackend, )
    filter_class = DealFilter

    def get_queryset(self):
        return Deal.objects.all()