"""ultrashop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .views import CategoryListView, ProductImagesView, ProductListView, PerksListView

urlpatterns = [
    path('categories', CategoryListView.as_view(), name='category-list'),
    path('productimages', ProductImagesView.as_view(), name='product-image-list'),
    path('perks', PerksListView.as_view(), name='product-perks-list'),
    path('', ProductListView.as_view(), name='product-list'),
]
