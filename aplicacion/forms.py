from django import forms
from .models import Persona, Producto

#Esto es para los formularios #falta completar funciones
class PersonaForm(forms.ModelForm):
    
    #VER CRUD DEL PROFE PARA TERMINAR 
    class Meta:
        model = Persona
        fields = []
    
class UpdatePersonaForm(forms.ModelForm):
    
    #VER CRUD DEL PROFE PARA TERMINAR 
    class Meta:
        model = Persona
        fields = []
        
class ProductoForm(forms.ModelForm):
    
    #VER CRUD DEL PROFE PARA TERMINAR 
    class Meta:
        model = Persona
        fields = []
        
class UpdateProductoForm(forms.ModelForm):
    
     #VER CRUD DEL PROFE PARA TERMINAR 
    class Meta:
        model = Persona
        fields = []