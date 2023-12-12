from django import forms

class ServicioForm(forms.Form):
    servicio = forms.CharField()
    descripcion = forms.CharField()
    precio = forms.IntegerField()

class VehiculoForm(forms.Form):
    vehiculo = forms.CharField()
    marca = forms.CharField()
    modelo = forms.CharField()

class TiendaForm(forms.Form):
    producto = forms.CharField()
    precio = forms.IntegerField()

class Filtro(forms.Form):
    nombre = forms.CharField()