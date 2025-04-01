from rest_framework import viewsets
from facturacion.models import Persona
from facturacion.serializers import PersonaSerializer


class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
