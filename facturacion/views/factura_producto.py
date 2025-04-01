from rest_framework import viewsets
from facturacion.models import FacturaProducto
from facturacion.serializers import FacturaProductoSerializer


class FacturaProductoViewSet(viewsets.ModelViewSet):
    queryset = FacturaProducto.objects.all()
    serializer_class = FacturaProductoSerializer
