from rest_framework import viewsets
from facturacion.models import Factura
from facturacion.serializers import FacturaSerializer, FacturaDetalleSerializer


class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaDetalleSerializer
