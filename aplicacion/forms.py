from django import forms
from .models import Persona, Producto

#Esto es para los formularios #falta completar funciones
class ProductoForm(forms.ModelForm):
    nombre = forms.CharField(max_length=50, error_messages= {"required":"Ingrese su nombre"}, 
                        help_text="Debe ingresar su nombre")
    tipo_producto = forms.CharField(max_length=50, error_messages= {"required":"Ingrese el tipo de producto"}, 
                        help_text="Debe ingresar que tipo de producto es")
    tipo_municion = forms.CharField(max_length=35, error_messages= {"required":"Ingrese el tipo de municion"}, 
                        help_text="Debe ingresar que tipo de  es")
    precio = forms.IntegerField(max_length="20", error_messages= {"required":"Ingrese el precio"}, 
                        help_text="Debe ingresar el valor del producto")
    #VER CRUD DEL PROFE PARA TERMINAR 
    class Meta:
        model = Persona
    fields = ['cod_producto',
              'nombre', 
              'tipo_producto',
              'tipo_municion']

class UpdateProductoForm(forms.ModelForm):
    
    #VER CRUD DEL PROFE PARA TERMINAR 
    class Meta:
        model = Persona
        fields = []