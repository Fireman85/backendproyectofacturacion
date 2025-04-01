from django.db import models


class Compania(models.Model):
    nit = models.CharField(max_length=45)
    nombre = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre
