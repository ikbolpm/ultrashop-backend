from rest_framework import serializers

from .models import GraphicsCardBrand


class GraphicsBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = GraphicsCardBrand
        fields = [
            'id',
            'name',
            'slug'
        ]
