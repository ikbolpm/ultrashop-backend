from rest_framework import serializers

from .models import LaptopType, ComputerPerk


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

class LaptopPerksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComputerPerk
        fields = [
            'id',
            'name',
            'slug'
        ]