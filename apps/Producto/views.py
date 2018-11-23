# Django
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib import messages
from django.db.models import Sum

# Modelos
from apps.Producto.models import Producto, Venta

# Forms
from apps.Producto.forms import FormProducto, FormVenta

# Create your views here.

# Productos
def index(request):
	contexto = { 
		'Producto': Producto.objects.all()
	}
	return render(request, 'producto/index.html', contexto)

def especial(request):
	return render(request, 'producto/plantillaClaseProducto.html')

def nuevoRegistro(request):
	if request.method == 'POST':
		form = FormProducto(request.POST)
		if form.is_valid():
			form.save()
		return redirect('vistaProductos')
	else:
		form = FormProducto()
	return render(request, 'producto/agregarProductoFormulario.html', {'form' : form})

def editarProducto(request, idProducto):
	producto = Producto.objects.get(id=idProducto)
	if (request.method == 'GET'):
		form = FormProducto(instance=producto)
	else:
		form = FormProducto(request.POST, instance=producto)
		if form.is_valid():
			form.save()
		return redirect('vistaProductos')
	return render(request, 'producto/agregarProductoFormulario.html', {'form' : form})

def eliminarProducto(request, idProducto):
	producto = Producto.objects.get(id=idProducto)
	if (request.method == 'GET'):
		instance = producto
		instance.delete()
	return redirect('vistaProductos')


# Ventas
def venta(request):
    lista = { 
		'productos': Venta.objects.all(),
        'total': sumar()
	}
    return render(request, 'venta/venta.html', lista)

def comprarProducto(request, idProducto):
    producto = Producto.objects.get(id=idProducto)
    producto2 = Producto.objects.filter(pk=idProducto).first()
    if(request.method == 'GET'):
        form = FormVenta(instance=producto)
    else: 
        form2= FormVenta(request.POST)
        if form2.is_valid():
            if(int(request.POST['cantidad']) <= producto.numExistencias):
                actualizado = producto.numExistencias - int(request.POST['cantidad'])
                producto2.numExistencias = actualizado
                total = int(producto.costo) * int(request.POST['cantidad']);
                prueba = form2.save(commit=False)
                prueba.total = total;
                prueba.save()
                producto2.save()
                messages.success(request, 'Se agrego a la lista.')
            elif(int(request.POST['cantidad']) > producto.numExistencias):
                messages.error(request, 'La cantidad excede las existencias.')          
        return redirect('ventas')   
    return render(request, 'producto/ventaFormulario.html', {'form' : form})

def pagar(request):
    ventas = Venta.objects.all()
    if(request.method == 'GET'):
        instance = ventas
        instance.delete()
        messages.success(request, 'Se realizo la compra.')
    return redirect('vistaProductos')

def sumar():
    suma = Venta.objects.all()
    total = 0
    for datos in suma:
        total = total + datos.total
    return total

# ListView productos
class viewProductos(ListView):
	model = Producto
	# queryset = Producto.objects.filter(nombreProducto='Doritos Nacho')
	queryset = Producto.objects.all()
	template_name = 'producto/plantillaClaseProducto.html'
