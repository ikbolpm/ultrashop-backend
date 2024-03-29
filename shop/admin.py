from django.contrib import admin
from django.shortcuts import get_object_or_404

from .models import Category, Product
from custom_multiupload.admin import MultiUploadAdmin
from .models import Image, Laptop, AllInOne, Desktop, Printer

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'slug']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name', 'part_number', 'upc']

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

class ImageInlineAdmin(admin.TabularInline):
    model = Image

class GalleryMultiuploadMixing(object):
    def process_uploaded_file(self, uploaded, gallery, request):
        if gallery:
            image = gallery.product_images.create(file=uploaded)
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
    list_display = ['brand', 'title', 'vat', 'price', 'ram', 'processor', 'ssd', 'hdd', 'screen_size',
                    'resolution', 'graphics_card', 'created', ]
    list_display_links = ['title', ]
    list_filter = (
        ('brand', admin.RelatedOnlyFieldListFilter),
        ('screen_size', admin.RelatedOnlyFieldListFilter),
        ('resolution', admin.RelatedOnlyFieldListFilter),
        ('processor', admin.RelatedOnlyFieldListFilter),
        ('graphics_card', admin.RelatedOnlyFieldListFilter),
    )
    save_as = True
    autocomplete_fields = ['processor', 'graphics_card', 'brand', 'category']
    search_fields = ['brand__name', 'graphics_card__name', 'resolution__name', 'processor__name', 'title', 'upc', 'part_number']
    inlines = [ImageInlineAdmin, ]
    multiupload_form = True
    multiupload_list = False
    exclude = ['type', 'slug', 'viewed', 'updated', 'created', 'description', ]

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
admin.site.register(Laptop, LaptopAdmin)

class AllInOneAdmin(GalleryMultiuploadMixing, MultiUploadAdmin):
    list_display = ['brand', 'title', 'vat', 'price', 'ram', 'processor', 'ssd', 'hdd', 'screen_size',
                    'resolution', 'graphics_card', 'created', ]
    list_display_links = ['title', ]
    list_filter = (
        ('brand', admin.RelatedOnlyFieldListFilter),
        ('screen_size', admin.RelatedOnlyFieldListFilter),
        ('resolution', admin.RelatedOnlyFieldListFilter),
        ('processor', admin.RelatedOnlyFieldListFilter),
        ('graphics_card', admin.RelatedOnlyFieldListFilter),
    )
    save_as = True
    autocomplete_fields = ['processor', 'graphics_card','brand', 'category']
    search_fields = ['brand__name', 'graphics_card__name', 'resolution__name', 'processor__name', 'title', 'upc', 'part_number']
    inlines = [ImageInlineAdmin, ]
    multiupload_form = True
    multiupload_list = False
    exclude = ['type', 'slug', 'viewed', 'updated', 'created', 'description', ]

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
admin.site.register(AllInOne, AllInOneAdmin)


class DesktopAdmin(GalleryMultiuploadMixing, MultiUploadAdmin):
    list_display = ['brand', 'title', 'vat', 'price', 'ram', 'processor', 'ssd', 'hdd', 'screen_size',
                    'resolution', 'graphics_card', 'created', ]
    list_display_links = ['title', ]
    list_filter = (
        ('brand', admin.RelatedOnlyFieldListFilter),
        ('screen_size', admin.RelatedOnlyFieldListFilter),
        ('resolution', admin.RelatedOnlyFieldListFilter),
        ('processor', admin.RelatedOnlyFieldListFilter),
        ('graphics_card', admin.RelatedOnlyFieldListFilter),
    )
    save_as = True
    autocomplete_fields = ['processor', 'graphics_card','brand', 'category']
    search_fields = ['brand__name', 'graphics_card__name', 'resolution__name', 'processor__name', 'title', 'upc', 'part_number']
    # prepopulated_fields = {'slug': ('name',),}
    inlines = [ImageInlineAdmin, ]
    multiupload_form = True
    multiupload_list = False
    exclude = ['type', 'slug', 'viewed', 'updated', 'created', 'description', ]

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
admin.site.register(Desktop, DesktopAdmin)


class PrinterAdmin(GalleryMultiuploadMixing, MultiUploadAdmin):
    list_display = ['title', 'speed', 'vat', 'price', 'created', ]
    list_display_links = ['title', ]
    list_filter = (
        'vat',
        ('brand', admin.RelatedOnlyFieldListFilter),
        ('formats', admin.RelatedOnlyFieldListFilter),
        ('technology', admin.RelatedOnlyFieldListFilter),
    )
    save_as = True
    search_fields = ['brand__name', 'color__name', 'title', 'name', 'upc', 'part_number']
    inlines = [ImageInlineAdmin, ]
    multiupload_form = True
    multiupload_list = False
    exclude = ['type', 'title', 'slug', 'viewed', 'updated', 'created',]

    def delete_file(self, pk, request):
        '''
        Delete an image.
        '''
        obj = get_object_or_404(Image, pk=pk)
        return obj.delete()
    def brand (self, instance):
        return instance.brand.name

    # def screen_size (self, instance):
    #     return instance.screen_size.name
admin.site.register(Printer, PrinterAdmin)


class ImageAdmin(GalleryMultiuploadMixing, MultiUploadAdmin):
    multiupload_form = False
    multiupload_list = True
    def get_model_perms(self, request):
        # Hide from Admin panel, still allowing to use from inline
        return {}

admin.site.register(Image, ImageAdmin)