from django.contrib import admin
from apps.Producto.models import Producto, Venta

# Register your models here.
admin.site.register(Producto)
admin.site.register(Venta)