from django.shortcuts import render, redirect
from apps.Categoria.models import Categoria
from django.views.generic import ListView
from apps.Categoria.forms import FormCategoria

# Create your views here.
def index(request):
	contexto = { 
		'Categoria': Categoria.objects.all()
	}
	return render(request, 'categoria/index.html', contexto)

def especial(request):
	return render(request, 'categoria/plantillaClaseCategoria.html')

def nuevoRegistro(request):
	if request.method == 'POST':
		form = FormCategoria(request.POST)
		if form.is_valid():
			form.save()
		return redirect('Categoria:vistaCategoria')
	else:
		form = FormCategoria()
	return render(request, 'categoria/agregarCategoriaFormulario.html', {'form' : form})

def editarCategoria(request, idCategoria):
	categoria = Categoria.objects.get(id=idCategoria)
	if (request.method == 'GET'):
		form = FormCategoria(instance=categoria)
	else:
		form = FormCategoria(request.POST, instance=categoria)
		if form.is_valid():
			form.save()
		return redirect('Categoria:vistaCategoria')
	return render(request, 'categoria/agregarCategoriaFormulario.html', {'form' : form})

def eliminarCategoria(request, idCategoria):
	categoria = Categoria.objects.get(id=idCategoria)
	if (request.method == 'GET'):
		instance = categoria
		instance.delete()
	return redirect('Categoria:vistaCategoria')

class viewCategoria(ListView):
	model = Categoria
	# queryset = Producto.objects.filter(nombreProducto='Doritos Nacho')
	queryset = Categoria.objects.all()
	template_name = 'categoria/plantillaClaseCategoria.html'