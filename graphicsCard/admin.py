from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import GraphicsCard

class GraphicsCardAdmin(ModelAdmin):
    list_display = ['name', 'brand', 'memory_interface', 'memory_interface_width']
    prepopulated_fields = {'slug': ('name',),}
    search_fields = ['name']

admin.site.register(GraphicsCard, GraphicsCardAdmin)