from django.db import models


class FacturaProducto(models.Model):
    producto = models.ForeignKey('productos.Producto',
                                 on_delete=models.PROTECT,
                                 related_name='factura_productos')
    factura = models.ForeignKey('Factura', on_delete=models.PROTECT,
                                null=True, related_name='factura_productos')
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
