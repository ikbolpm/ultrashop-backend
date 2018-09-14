from rest_framework import serializers

from .models import Resolution


class ResolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resolution
        fields = [
            'id',
            'name',
            'size'
        ]
