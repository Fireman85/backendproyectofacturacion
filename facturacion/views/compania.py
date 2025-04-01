from rest_framework import viewsets
from facturacion.models import Compania
from facturacion.serializers import CompaniaSerializer


class CompaniaViewSet(viewsets.ModelViewSet):
    queryset = Compania.objects.all()
    serializer_class = CompaniaSerializer
