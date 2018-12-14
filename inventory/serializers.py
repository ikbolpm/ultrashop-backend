from rest_framework import serializers

from .models import Inventory


class InventorySerializer(serializers.ModelSerializer):
    laptop_id = serializers.SerializerMethodField()
    class Meta:
        model = Inventory
        fields = [
            'laptop_id',
            'quantity'
        ]

    def get_laptop_id(self, obj):
        return obj.get('laptop')