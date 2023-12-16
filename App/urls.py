from django.contrib import admin
from django.urls import path
from App.views import show_html, mostrar_producto_tienda, mostrar_servicio, mostrar_vehiculo, agregar_producto_tienda, \
    agregar_servicio, agregar_vehiculo, filtrar_producto_tienda, filtrar_servicio, filtrar_vehiculo, VehiculoList, \
    VehiculoDetalle

urlpatterns = [
    path('show/', show_html),
    path('servicios/', mostrar_servicio),
    path('vehiculos/', mostrar_vehiculo),
    path('catalogo_tienda/', mostrar_producto_tienda),
    path('agregar_servicio/', agregar_servicio),
    path('agregar_vehiculo/', agregar_vehiculo),
    path('agregar_producto/', agregar_producto_tienda),
    path('filtrar_servicios/', filtrar_servicio),
    path('filtrar_vehiculos/', filtrar_vehiculo),
    path('filtrar_producto_catalogo/', filtrar_producto_tienda),
    path('vehiculos/listar', VehiculoList.as_view(),),
    path('vehiculo/<int:pk>', VehiculoDetalle.as_view(),),

]
