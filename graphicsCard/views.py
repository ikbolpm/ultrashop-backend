from rest_framework import generics

from .models import GraphicsCard
from .serializers import GraphicsSerializer


class GraphicsListView(generics.ListAPIView):
    serializer_class = GraphicsSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return GraphicsCard.objects.all()
