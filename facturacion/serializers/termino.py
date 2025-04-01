from rest_framework import serializers
from facturacion.models import Termino


class TerminoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Termino
        fields = '__all__'
