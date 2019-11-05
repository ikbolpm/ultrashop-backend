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
    path('api/inventory', include('inventory.urls')),
    path('api/products/', include('products.ulrs')),
    path('tinymce/', include('tinymce.urls')),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
