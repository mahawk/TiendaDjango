# Django
from django.db import models

# Modelo del producto
class Producto(models.Model):
	nombreProducto = models.CharField(max_length=30)
	descripcion = models.CharField(max_length=60)
	costo = models.DecimalField(max_digits=6, decimal_places=2)
	disponible = models.NullBooleanField()
	numExistencias = models.IntegerField(default = 0)

# Modelo de la venta
class Venta(models.Model):
    nombreProducto = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=60)
    costo = models.IntegerField(default=0)
    cantidad = models.IntegerField(default=0)
    total = models.IntegerField(default=0)