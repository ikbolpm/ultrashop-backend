from rest_framework.serializers import ModelSerializer
from .models import Inquiry, ProductInquiry


class InquiryCreateSerializer(ModelSerializer):
    class Meta:
        model = Inquiry
        fields = [
            'name',
            'phone',
            'laptop',
            'status',
            'description'
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