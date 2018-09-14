from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from .models import Inquiry
from .serializers import InquiryCreateSerializer

class InquiryCreateAPIView(CreateAPIView):
    serializer_class = InquiryCreateSerializer
    queryset = Inquiry.objects.all()