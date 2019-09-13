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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include


from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/laptops', include('laptop.urls')),
    path('api/products/', include('products.urls')),
    path('api/audio', include('audio.urls')),
    path('api/brand', include('brand.urls')),
    path('api/display', include('displaySize.urls')),
    path('api/graphics', include('graphicsCard.urls')),
    path('api/graphics-brands', include('graphicsCardBrand.urls')),
    path('api/laptop-types', include('laptopType.urls')),
    path('api/perks', include('perks.urls')),
    path('api/processors', include('processor.urls')),
    path('api/processor-brands', include('processorBrand.urls')),
    path('api/rams', include('ram.urls')),
    path('api/resolutions', include('resolution.urls')),
    path('api/storages', include('storage.urls')),
    path('api/inquiry/', include('inquiries.urls')),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refreh', TokenRefreshView.as_view()),
    # path('api/users/', include('accounts.urls')),
    path('api/inquiries/', include('inquiries.urls')),
    path('api/dollar', include('settings.urls')),
    path('api/inventory', include('inventory.urls'))
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
