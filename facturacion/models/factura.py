from django.db import models


class Factura(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    persona = models.ForeignKey('Persona', on_delete=models.PROTECT,
                                related_name='facturas')
    compania = models.ForeignKey('Compania', on_delete=models.PROTECT,
                                 null=True, related_name='facturas')
    termino = models.ForeignKey('Termino', on_delete=models.PROTECT,
                                related_name='facturas')

    def __str__(self):
        return str(self.id) + ' ' + self.persona.nombres
