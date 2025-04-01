from rest_framework import serializers
from facturacion.models import Factura


class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = ['fecha', 'persona', 'compania', 'termino']
