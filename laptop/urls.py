from django.urls import path

from .views import LaptopListView, LaptopImagesView

urlpatterns = [
    path('laptopimages', LaptopImagesView.as_view(), name='laptop-image-list'),
    path('', LaptopListView.as_view(), name='laptop-list'),
]
