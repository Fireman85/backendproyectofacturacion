from rest_framework import serializers
from productos.models import Producto


class ProductoSerializer(serializers.ModelSerializer):
    nombre_categoria = serializers.StringRelatedField(source='categoria',
                                                      read_only=True)

    class Meta:
        model = Producto
        fields = '__all__'
