from rest_framework import serializers
from facturacion.models import FacturaProducto


class FacturaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacturaProducto
        fields = ['producto', 'cantidad']
