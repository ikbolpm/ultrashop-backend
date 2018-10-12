from rest_framework import serializers

from .models import LaptopType


class LaptopTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaptopType
        fields = [
            'id',
            'name',
            'slug',
            'name_singular',
            'logo',
            'short_description'
        ]