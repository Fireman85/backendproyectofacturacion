from rest_framework import viewsets
from facturacion.models import Termino
from facturacion.serializers import TerminoSerializer


class TerminoViewSet(viewsets.ModelViewSet):
    queryset = Termino.objects.all()
    serializer_class = TerminoSerializer
