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


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = ['brand__name', 'category__name', 'name', 'model', 'old_price', 'price']

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"


class ProductAdmin(GalleryMultiuploadMixing, MultiUploadAdmin, ExportCsvMixin):
    list_display = ['brand', 'category', 'name', 'model', 'vat', 'price', 'old_price', 'created', ]
    list_editable = ['old_price', 'price']
    list_display_links = ['name', ]
    list_filter = (
        ('brand', admin.RelatedOnlyFieldListFilter),
        ('category', admin.RelatedOnlyFieldListFilter),
    )
    # autocomplete_fields = ['processor']
    search_fields = ['brand__name', 'name', 'category__name', 'model', ]
    prepopulated_fields = {'slug': ('name',),}
    inlines = [ImageInlineAdmin, ]
    multiupload_form = True
    multiupload_list = False
    actions = ["export_as_csv"]
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