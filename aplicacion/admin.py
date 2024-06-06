from django.contrib import admin
from .models import Persona, Usuario, Envio, Producto
# Register your models here.

class AdmPersona(admin.ModelAdmin):
    list_display=['pnombre','snombre','apellidop', 'apellidom', 'correo', 'direccion', 'celular', 'region', 'info_adicional', 'imagen']
    list_editable=['snombre','apellidop', 'apellidom', 'correo', 'direccion', 'celular', 'region', 'info_adicional', 'imagen']
    list_filter= ['pnombre', 'apellidop']
    
class AdmUsuario (admin.ModelAdmin):
    list_display = ['nombusuario']
    list_filter = ['nombusuario']

class AdmEnvio(admin.ModelAdmin):
    list_display = ['idcompra', 'fecha_compra', 'estado', 'usuario', 'imagenenvio']
    list_editable = ['estado']
    list_filter = ['fecha_compra', 'estado', 'usuario']
    
class AdmProducto(admin.ModelAdmin):
    list_display = ['nombre', 'tipo_producto', 'tipo_municion', 'precio', 'stock', 'image']
    list_editable = ['tipo_producto', 'tipo_producto', 'tipo_municion', 'precio', 'stock', 'image']
    list_filter = ['nombre', 'tipo_producto', 'tipo_municion'] 