from rest_framework import serializers
from facturacion.models import Factura, FacturaProducto
from productos.models import Producto
from .factura_producto import FacturaProductoDetalleSerializer


class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = ['fecha', 'persona', 'compania', 'termino']


class FacturaDetalleSerializer(serializers.ModelSerializer):
    factura_productos = FacturaProductoDetalleSerializer(many=True)
    nombre_persona = serializers.StringRelatedField(source='persona',
                                                    read_only=True)
    nombre_compania = serializers.StringRelatedField(source='compania',
                                                     read_only=True)
    nombre_termino = serializers.StringRelatedField(source='termino',
                                                    read_only=True)

    class Meta:
        model = Factura
        fields = ['id', 'fecha', 'persona', 'compania', 'termino',
                  'factura_productos', 'nombre_persona', 'nombre_compania',
                  'nombre_termino']

    def create(self, validated_data):
        # extraer detalles de la factura
        detalles_data = validated_data.pop('factura_productos')

        # crear factura
        factura = Factura.objects.create(**validated_data)

        # crear detalle de la factura
        for detalle in detalles_data:
            print("detalle ", detalle)
            producto = Producto.objects.get(id=detalle['producto'].id)
            FacturaProducto.objects.create(
                factura=factura,
                valor_unitario=producto.valor_unitario_venta,
                **detalle
            )

        return factura
