
from rest_framework import viewsets

# mi modelo creado
from productos.models import Categoria
# mi serializer creado
from productos.serializers import CategoriaSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
