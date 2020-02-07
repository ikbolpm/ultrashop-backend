from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import GraphicsCard

class GraphicsCardAdmin(ModelAdmin):
    list_display = ['name', 'brand', 'memory_interface', 'memory_interface_width']
    prepopulated_fields = {'slug': ('name',),}
    search_fields = ['name']
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

admin.site.register(GraphicsCard, GraphicsCardAdmin)