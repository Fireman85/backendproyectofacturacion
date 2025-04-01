from django.db import models


class Termino(models.Model):
    nombre = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre
