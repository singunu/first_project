from rest_framework import serializers
from .models import ExchangeRate

class exchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRate
        fields = '__all__'