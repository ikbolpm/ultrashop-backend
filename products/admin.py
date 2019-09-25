from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.shortcuts import get_object_or_404
from custom_multiupload.admin import MultiUploadAdmin
from django.conf import settings


from .models import Category, Image, Product, Perks


class CategoryAdmin (ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',), }

admin.site.register(Category, CategoryAdmin)


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


class ProductAdmin(GalleryMultiuploadMixing, MultiUploadAdmin):
    list_display = ['brand', 'category', 'name', 'model', 'vat', 'price', 'created', ]
    list_display_links = ['name', ]
    list_filter = (
        ('brand', admin.RelatedOnlyFieldListFilter),
        ('category', admin.RelatedOnlyFieldListFilter),
    )
    # autocomplete_fields = ['processor']
    # search_fields = ['brand__name', 'graphics_card__name', 'resolution__name', 'processor__name', 'name', 'model', 'upc']
    prepopulated_fields = {'slug': ('name',),}
    inlines = [ImageInlineAdmin, ]
    multiupload_form = True
    multiupload_list = False
    save_as = True

    def delete_file(self, pk, request):
        '''
        Delete an image.
        '''
        obj = get_object_or_404(Image, pk=pk)
        return obj.delete()
    def brand (self, instance):
        return instance.brand.name
    def category (self, instance):
        return instance.category.name

class ImageAdmin(GalleryMultiuploadMixing, MultiUploadAdmin):
    multiupload_form = False
    multiupload_list = True

admin.site.register(Product, ProductAdmin)
admin.site.register(Image, ImageAdmin)

class PerksAdmin(ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',), }


admin.site.register(Perks, PerksAdmin)