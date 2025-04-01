from django.db import models


class Producto(models.Model):
    categoria = models.ForeignKey('Categoria', on_delete=models.PROTECT)
    nombre = models.CharField(max_length=150)
    existencia = models.IntegerField(default=0)
    valor_unitario_venta = models.FloatField(default=0.0)
    valor_unitario_compra = models.FloatField(default=0.0)

    def __str__(self):
        return self.nombre
