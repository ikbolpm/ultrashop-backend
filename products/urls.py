from django.urls import path

from .views import CategoryListAPIView, BrandListAPIView, ProductListAPIView

urlpatterns = [
    path('brands', BrandListAPIView.as_view(), name='brand-list'),
    path('categories', CategoryListAPIView.as_view(), name='category-list'),
    path('list', ProductListAPIView.as_view(), name='product-list'),
]
