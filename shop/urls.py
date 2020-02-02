from django.urls import path
from .views import ImageListApiView, ProductListApiView, CategoryListApiView
urlpatterns = [
    # path('', views.product_list, name='product_list'),
    # path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    # path('<slug:category_slug>/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('category', CategoryListApiView.as_view(), name='product-category-list'),
    path('product-images', ImageListApiView.as_view(), name='product-image-list'),
    path('', ProductListApiView.as_view(), name='product-list'),
]