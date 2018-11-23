from django.urls import path
from apps.Categoria.views import index, especial, viewCategoria, nuevoRegistro, editarCategoria, eliminarCategoria

app_name = "Categoria"
urlpatterns = [
	path('', index),
	path('index', index),
	path('especial', viewCategoria.as_view(), name='vistaCategoria'),
	path('nuevoRegistro', nuevoRegistro, name="nuevoRegistro"),
	path('editarProducto/<idCategoria>', editarCategoria, name="editarCategoria"),
	path('eliminarProducto/<idCategoria>', eliminarCategoria, name="eliminarCategoria"),
]