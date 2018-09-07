from rest_framework import serializers

from .models import DisplaySize


class DisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = DisplaySize
        fields = [
            'id',
            'size'
        ]
