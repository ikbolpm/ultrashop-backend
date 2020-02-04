from rest_framework.serializers import ModelSerializer
from .models import Inquiry


class InquiryCreateSerializer(ModelSerializer):
    class Meta:
        model = Inquiry
        fields = [
            'name',
            'phone',
            'inquired_product',
            'status',
            'description'
        ]