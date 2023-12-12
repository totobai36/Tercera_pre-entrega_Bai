from django.shortcuts import render, redirect
from App.models import Vehiculo, Servicio, Tienda
from App.forms import ServicioForm, TiendaForm, VehiculoForm, Filtro
# Create your views here.
def show_html(request):
    contexto = {}
    return render(request, 'index.html', contexto)

def agregar_vehiculo(request):
    if request.method == "POST":
        vehiculo_formulario = VehiculoForm(request.POST)
        if vehiculo_formulario.is_valid():
            informacion = vehiculo_formulario.cleaned_data
            vehiculo_agregar = Vehiculo(vehiculo=informacion["vehiculo"], marca=informacion["marca"], modelo=informacion["modelo"])
            vehiculo_agregar.save()

            return redirect("/app/vehiculos")

    vehiculo_form = VehiculoForm()
    contexto = {
        "form": vehiculo_form
    }

    return render(request, "App/agregar_vehiculo.html", contexto)

def mostrar_vehiculo(request):
    vehiculos = Vehiculo.objects.all()
    contexto = {
        "Vehiculos": vehiculos,
        "form": Filtro()
    }

    return render(request, 'App/vehiculos.html', contexto)

def filtrar_vehiculo(request):
    vehiculo = request.GET["vehiculo"]
    vehiculos = Vehiculo.objects.filter(vehiculo__icontains=vehiculo)


    contexto = {
        "vehiculos": vehiculos,
        "form": Filtro()
    }

    return render(request, 'app/vehiculos.html', contexto)



def agregar_servicio(request):
    if request.method == "POST":
        servicio_formulario = ServicioForm(request.POST)
        if servicio_formulario.is_valid():
            informacion = servicio_formulario.cleaned_data
            servicio_agregar = Servicio(servicio=informacion["servicio"], descripcion=informacion["descripcion"], precio=informacion["precio"])
            servicio_agregar.save()

            return redirect("/app/servicios")

    servicio_form = ServicioForm()
    contexto = {
        "form": servicio_form
    }

    return render(request, "App/agregar_servicio.html", contexto)
def mostrar_servicio(request):
    servicios = Servicio.objects.all()
    contexto = {
        "servicios": servicios,
        "form": Filtro()
    }

    return render(request, 'App/servicios.html', contexto)
def filtrar_servicio(request):
    servicio = request.GET["servicio"]
    servicios = Servicio.objects.filter(servicio__icontains=servicio)

    contexto = {
        "servicios": servicios,
        "form": Filtro()
    }

    return render(request, 'app/servicios.html', contexto)



def agregar_producto_tienda(request):
    if request.method == "POST":
        producto_form = TiendaForm(request.POST)
        if producto_form.is_valid():
            informacion = producto_form.cleaned_data
            producto_agregar = Tienda(producto=informacion["producto"], precio=informacion["precio"])
            producto_agregar.save()

            return redirect("/app/catalogo_tienda")

    producto_form = TiendaForm()

    contexto = {
        "form": producto_form
    }

    return render(request, 'App/agregar_producto_tienda.html', contexto)
def mostrar_producto_tienda(request):
    productos = Tienda.objects.all()
    contexto = {
        "productos": productos,
        "form": Filtro()
    }

    return render(request, 'App/productos.html', contexto)


def filtrar_producto_tienda(request):
    producto = request.GET["producto"]
    productos = Tienda.objects.filter(producto__icontains=producto)

    contexto = {
        "productos": productos,
        "form": Filtro()
    }

    return render(request, 'App/productos.html', contexto)
