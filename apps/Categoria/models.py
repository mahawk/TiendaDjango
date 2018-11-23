from django.db import models
from apps.Producto.models import Producto

class Categoria(models.Model):
	nombreCategoria = models.CharField(max_length=20)
	fechaCreacion = models.DateField(default = '2000-01-01')
	producto = models.ForeignKey(Producto, null=True, blank=True, on_delete = models.CASCADE)
