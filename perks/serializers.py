from rest_framework import serializers

from .models import Perks


class PerksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perks
        fields = [
            'id',
            'name',
            'slug'
        ]
