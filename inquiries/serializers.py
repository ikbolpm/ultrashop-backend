from rest_framework.serializers import ModelSerializer
from .models import Inquiry, ProductInquiry

class InquiryCreateSerializer(ModelSerializer):
    class Meta:
        model = Inquiry
        fields = [
            'name',
            'phone',
            'comments',
            'size',
            'ram',
            'resolution',
            'storage',
            'type',
            'source',
            'laptop',
            'processor',
            'min_price',
            'max_price',
            'min_cores',
            'max_cores',
            'min_size',
            'max_size',
            'min_storage',
            'max_storage',
            'min_ram',
            'max_ram',
        ]


class ProductInquiryCreateSerializer(ModelSerializer):
    class Meta:
        model = ProductInquiry
        fields = [
            'name',
            'phone',
            'source',
            'product',
        ]