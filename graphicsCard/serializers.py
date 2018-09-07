from rest_framework import serializers

from graphicsCardBrand.models import GraphicsCardBrand
from .models import GraphicsCard


class GraphicsBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = GraphicsCardBrand
        fields = ['id', 'name', 'slug']


class GraphicsSerializer(serializers.ModelSerializer):
    brand = GraphicsBrandSerializer()

    class Meta:
        model = GraphicsCard
        fields = ['id', 'name', 'slug', 'brand', 'memory_interface', 'memory_interface_width']
