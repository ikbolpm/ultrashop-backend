from rest_framework.generics import CreateAPIView

from .models import Inquiry, ProductInquiry
from .serializers import InquiryCreateSerializer, ProductInquiryCreateSerializer

class InquiryCreateAPIView(CreateAPIView):
    serializer_class = InquiryCreateSerializer
    queryset = Inquiry.objects.all()


class ProductInquiryCreateAPIView(CreateAPIView):
    serializer_class = ProductInquiryCreateSerializer
    queryset = ProductInquiry.objects.all()