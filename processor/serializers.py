from rest_framework import serializers

from processorBrand.models import ProcessorBrand
from .models import Processor


class ProcessorBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessorBrand
        fields = ['id', 'name']


class ProcessorSerializer(serializers.ModelSerializer):
    brand = ProcessorBrandSerializer()

    class Meta:
        model = Processor
        fields = ['id', 'name', 'brand', 'min_frequency', 'max_frequency', 'cores', 'threads', 'cache',
                  'integrated_graphics']
