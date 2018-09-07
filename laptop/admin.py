from django.contrib import admin
from django.shortcuts import get_object_or_404
from multiupload.admin import MultiUploadAdmin

from ultrashop.settings import BASE_URL
from .models import Laptop, Image


class ImageInlineAdmin(admin.TabularInline):
    model = Image

class GalleryMultiuploadMixing(object):

    def process_uploaded_file(self, uploaded, gallery, request):
        if gallery:
            image = gallery.images.create(file=uploaded)
        else:
            image = Image.objects.create(file=uploaded, gallery=None)
        return {
            'url': image.file.url,
            'absolute_url': BASE_URL + image.file.url,
            'thumbnail_url': image.file.url,
            'id': image.id,
            'name': image.filename
        }



class LaptopAdmin(GalleryMultiuploadMixing, MultiUploadAdmin):
    list_display = ['name', 'brand', 'ram', 'processor', 'main_storage', 'secondary_storage', 'screen_size',
                    'resolution', 'graphics_card', 'price', 'created', ]
    list_editable = ['brand', 'ram', 'processor', 'main_storage', 'secondary_storage', 'screen_size', 'resolution',
                     'graphics_card', 'price']
    list_display_links = ['name', ]
    list_filter = ['brand', ]
    search_fields = ['graphics_card', 'resolution', 'processor']
    prepopulated_fields = {'slug': ('name',),}
    inlines = [ImageInlineAdmin, ]
    multiupload_form = True
    multiupload_list = False

    def delete_file(self, pk, request):
        '''
        Delete an image.
        '''
        obj = get_object_or_404(Image, pk=pk)
        return obj.delete()
    def brand (self, instance):
        return instance.brand.name

    def screen_size (self, instance):
        return instance.screen_size.name

class ImageAdmin(GalleryMultiuploadMixing, MultiUploadAdmin):
    multiupload_form = False
    multiupload_list = True

admin.site.register(Laptop, LaptopAdmin)
admin.site.register(Image, ImageAdmin)