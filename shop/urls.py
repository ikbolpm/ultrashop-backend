from django.urls import path
from .views import ImageListApiView, ProductListApiView, CategoryListApiView, LaptopListApiView
urlpatterns = [
    path('category', CategoryListApiView.as_view(), name='product-category-list'),
    path('images', ImageListApiView.as_view(), name='product-image-list'),
    path('noutbuki', LaptopListApiView.as_view(), name='laptop-list'),
    path('', ProductListApiView.as_view(), name='product-list'),
]