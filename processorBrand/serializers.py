from rest_framework import serializers

from .models import ProcessorBrand


class ProcessorBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessorBrand
        fields = [
            'id',
            'name',
            'slug'
        ]
