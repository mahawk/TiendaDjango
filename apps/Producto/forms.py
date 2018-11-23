# Django
from django import forms

# Modelos
from apps.Producto.models import Producto, Venta

# Formulario producto
class FormProducto(forms.ModelForm):
	class Meta:
		model = Producto

		fields = [
			'nombreProducto',
			'descripcion',
			'costo',
			'disponible',
			'numExistencias',
		]

		labels = {
			'nombreProducto' : 'Nombre producto',
			'descripcion' : 'Descripcion',
			'costo' : 'Costo',
			'disponible' : 'Disponibilidad',
			'numExistencias' : 'Número de existencias',
		}

		widgets = {
			'nombreProducto' : forms.TextInput(attrs={'class' : 'form-control'}),
			'descripcion' : forms.TextInput(attrs={'class' : 'form-control'}),
			'costo' : forms.TextInput(attrs={'class' : 'form-control'}),
			'disponible' : forms.TextInput(attrs={'class' : 'form-control'}),
			'numExistencias' : forms.TextInput(attrs={'class' : 'form-control'}),
		}

# Formulario venta
class FormVenta(forms.ModelForm):
    class Meta():
        model = Venta

        fields = [
            'nombreProducto',
            'descripcion',
            'costo',
            'cantidad',
            'total',
        ]

        labels = {
            'nombreProducto': 'Nombre producto', 
            'descripcion': 'Descripcion',
            'costo' : 'Costo',
            'cantidad': 'Cantidad',
            'total': 'Total',
        }

        widgets = {
            'nombreProducto':forms.TextInput(attrs={'class': 'form-control', 'readonly':'True'}),
            'descripcion':forms.TextInput(attrs={'class': 'form-control', 'readonly':'True'}),
            'costo':forms.NumberInput(attrs={'class': 'form-control', 'readonly':'True'}),
            'cantidad':forms.NumberInput(attrs={'class': 'form-control'}),
            'total':forms.NumberInput(attrs={'class': 'form-control', 'readonly':'True'}),
        }