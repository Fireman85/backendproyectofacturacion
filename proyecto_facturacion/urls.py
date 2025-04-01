"""
URL configuration for proyecto_facturacion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from productos.views import CategoriaViewSet, ProductoViewSet
from facturacion.views import (TerminoViewSet, PersonaViewSet,
                               CompaniaViewSet, FacturaViewSet,
                               FacturaProductoViewSet)


router = DefaultRouter()
router.register('categorias', CategoriaViewSet, 'view_categoria')
router.register('productos', ProductoViewSet, 'view_productos')
router.register('terminos', TerminoViewSet, 'view_termino')
router.register('personas', PersonaViewSet, 'view_persona')
router.register('compania', CompaniaViewSet, 'view_compania')
router.register('factura', FacturaViewSet, 'view_factura')
router.register('factura-producto', FacturaProductoViewSet,
                'view_factura_producto')


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
