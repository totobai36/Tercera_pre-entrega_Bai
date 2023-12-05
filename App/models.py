from django.db import models

class Servicio(models.Model):
    nombre = models.CharField(max_length=30, unique=True)
    descripcion = models.CharField(max_length=50)
    precio = models.IntegerField()