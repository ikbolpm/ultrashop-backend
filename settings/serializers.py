from rest_framework import serializers

from .models import DollarExchangeRate

class DollarExchangeRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DollarExchangeRate
        fields = ('exchange_rate', )