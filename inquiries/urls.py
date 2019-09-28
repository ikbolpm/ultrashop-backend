from django.urls import path

from .views import InquiryCreateAPIView, ProductInquiryCreateAPIView

urlpatterns = [
    path('createproduct', ProductInquiryCreateAPIView.as_view(), name='product-inquiry-create'),
    path('create', InquiryCreateAPIView.as_view(), name='inquiry-create'),
]
