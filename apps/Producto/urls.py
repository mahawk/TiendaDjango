from django.urls import path
from apps.Producto.views import index, especial, viewProductos, nuevoRegistro, editarProducto, eliminarProducto, venta, comprarProducto, pagar

urlpatterns = [
	path('index', index),
	path('', index, name='index'),
	path('especial', viewProductos.as_view(), name='vistaProductos'),
	path('nuevoRegistro', nuevoRegistro, name="nuevoRegistro"),
	path('editarProducto/<idProducto>', editarProducto, name="editarProducto"),
	path('eliminarProducto/<idProducto>', eliminarProducto, name="eliminarProducto"),
	path('comprarProducto/<idProducto>', comprarProducto, name="comprarProducto"),
	path('venta', venta, name ="ventas"),
    path('pagar', pagar, name="pagar"),
]