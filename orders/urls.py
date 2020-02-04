from django.urls import path

from .views import InquiryCreateAPIView

urlpatterns = [
    path('create-inquiry', InquiryCreateAPIView.as_view(), name='inquiry-create'),
]
