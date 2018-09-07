from rest_framework import generics

from .models import Resolution
from .serializers import ResolutionSerializer


class ResolutionListView(generics.ListAPIView):
    serializer_class = ResolutionSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Resolution.objects.all()
