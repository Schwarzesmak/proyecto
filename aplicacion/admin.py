from django.contrib import admin
from .models import Persona, Usuario, Envio, Producto, Carrito, Pedido, Perfil, DetallePedido
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
    list_display = ['cod_producto','nombre', 'tipo_producto', 'tipo_municion', 'precio', 'stock', 'imagen']
    list_editable = ['tipo_producto', 'tipo_producto', 'tipo_municion', 'precio', 'stock', 'imagen']
    list_filter = ['cod_producto','nombre', 'tipo_producto', 'tipo_municion']
    
class AdmCarrito(admin.ModelAdmin):
    list_display = ['usuario', 'producto', 'cantidad']
    list_editable = [ 'producto', 'cantidad']
    list_filter = ['usuario', 'producto', 'cantidad']
    
class AdmPedido(admin.ModelAdmin):
    list_display = ['usuario','id', 'nombre_cliente', 'direccion', 'correo', 'celular', 'region', 'fecha_pedido', 'estado']
    list_filter = ['region', 'estado']
    list_editable = ['nombre_cliente', 'direccion', 'correo', 'celular', 'estado']
    readonly_fields = ['id', 'fecha_pedido']
    
class AdmDetallePedido(admin.ModelAdmin):
    list_display    = ['pedido','producto','cantidad']

admin.site.register(Pedido, AdmPedido)
admin.site.register(DetallePedido)
admin.site.register(Persona,AdmPersona)
admin.site.register(Usuario,AdmUsuario)
admin.site.register(Envio,AdmEnvio)
admin.site.register(Producto,AdmProducto)
admin.site.register(Carrito,AdmCarrito)
admin.site.register(Perfil)






