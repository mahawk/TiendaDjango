from django import forms
from apps.Categoria.models import Categoria

class FormCategoria(forms.ModelForm):
	class Meta:
		model = Categoria

		fields = [
			'nombreCategoria',
			'fechaCreacion',
		]

		labels = {
			'nombreCategoria' : 'Nombre categoria',
			'fechaCreacion' : 'Fecha de creación',
		}

		widgets = {
			'nombreCategoria' : forms.TextInput(attrs={'class' : 'form-control'}),
			'fechaCreacion' : forms.TextInput(attrs={'class' : 'form-control'}),
		}