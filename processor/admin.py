from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Processor

class ProcessorAdmin(ModelAdmin):
    list_display = ['name', 'brand', 'min_frequency', 'max_frequency', 'cache', 'cores', 'threads', 'integrated_graphics']
    prepopulated_fields = {'slug': ('name',),}
    search_fields = ['name']
    def brand (self, instance):
        return instance.brand.name
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
admin.site.register(Processor, ProcessorAdmin)
