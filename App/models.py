from django.db import models

class Servicio(models.Model):
    servicio = models.CharField(max_length=30, unique=True)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()

    def __str__(self):
        return f"Servicio: {self.servicio}, Precio: {self.precio}"

class Vehiculo(models.Model):
    vehiculo = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)

    def __str__(self):
        return f"Vehiculo: {self.vehiculo}, Marca: {self.marca}, Modelo: {self.modelo}"

class Tienda(models.Model):
    producto = models.CharField(max_length=30, unique=True)
    precio = models.IntegerField()

    def __str__(self):
        return f"{self.producto}, sale ${self.precio}"