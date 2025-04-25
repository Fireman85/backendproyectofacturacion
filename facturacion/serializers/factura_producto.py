from rest_framework import serializers
from facturacion.models import FacturaProducto


class FacturaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacturaProducto
        fields = '__all__'


class FacturaProductoDetalleSerializer(serializers.ModelSerializer):
    nombre_producto = serializers.StringRelatedField(source='producto',
                                                     read_only=True)

    class Meta:
        model = FacturaProducto
        fields = ['producto', 'cantidad', 'nombre_producto']
