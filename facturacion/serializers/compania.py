from rest_framework import serializers
from facturacion.models import Compania


class CompaniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compania
        fields = '__all__'
