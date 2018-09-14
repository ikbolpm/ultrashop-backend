from rest_framework import generics

from .models import GraphicsCardBrand
from .serializers import GraphicsBrandSerializer


class GraphicsBrandListView(generics.ListAPIView):
    serializer_class = GraphicsBrandSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return GraphicsCardBrand.objects.all()
