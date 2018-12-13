from django.contrib import admin
from django.shortcuts import get_object_or_404
from custom_multiupload.admin import MultiUploadAdmin
from django.conf import settings

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
            'absolute_url': image.file.url,
            'thumbnail_url': image.file.url,
            'id': image.id,
            'name': image.filename
        }



class LaptopAdmin(GalleryMultiuploadMixing, MultiUploadAdmin):
    list_display = ['brand', 'name', 'model', 'price', 'ram', 'processor', 'main_storage', 'secondary_storage', 'screen_size',
                    'resolution', 'graphics_card', 'created', ]
    list_editable = ['brand', 'ram', 'processor', 'main_storage', 'secondary_storage', 'screen_size', 'resolution',
                     'graphics_card', 'price']
    list_display_links = ['name', ]
    # list_filter = ['brand', 'screen_size', 'resolution', 'graphics_card']
    list_filter = (
        ('brand', admin.RelatedOnlyFieldListFilter),
        ('screen_size', admin.RelatedOnlyFieldListFilter),
        ('resolution', admin.RelatedOnlyFieldListFilter),
        ('processor', admin.RelatedOnlyFieldListFilter),
        ('graphics_card', admin.RelatedOnlyFieldListFilter),
    )
    autocomplete_fields = ['processor']
    search_fields = ['brand__name', 'graphics_card__name', 'resolution__name', 'processor__name', 'name', 'model']
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
