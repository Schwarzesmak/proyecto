from django.shortcuts import render
#desde el crud del profe
from django.shortcuts import get_object_or_404, redirect
from .models import Persona, Producto, Envio #Carrito, Usuario
#importar forms.py tambien, falta
from .forms import PersonaForm, UpdatePersonaForm, ProductoForm, UpdateProductoForm #para formularios de persona y productos

# Create your views here.
def index (request):
    return render(request, "aplicacion/index.html")

def beretta (request):
    return render(request, "aplicacion/producto/beretta.html")
def camisa (request):
    return render(request, "aplicacion/producto/camisa.html")
def carpa (request):
    return render(request, "aplicacion/producto/carpa.html")
def casco (request):
    return render(request, "aplicacion/producto/casco.html")
def chaleco (request):
    return render(request, "aplicacion/producto/chaleco.html")
def cuchillo (request):
    return render(request, "aplicacion/producto/cuchillo.html")
def pantalon (request):
    return render(request, "aplicacion/producto/pantalon.html")
def valken (request):
    return render(request, "aplicacion/producto/valken.html")

#Aqui es para las paginas
def about (request):
    return render(request, "aplicacion/about.html")
def admini (request):
    return render(request, "aplicacion/admini.html")
def cart (request):
    return render(request, "aplicacion/cart.html")
def checkout (request):
    return render(request, "aplicacion/checkout.html")
def estado (request):
    return render(request, "aplicacion/estado.html")
def miscompras  (request):
    return render(request, "aplicacion/miscompras.html")
def panelcerrarsesion (request):
    return render(request, "aplicacion/panelcerrarsesion.html")
def panelcontrol (request):
    return render(request, "aplicacion/panelcontrol.html")
def panelcontrolestadocompra (request):
    return render(request, "aplicacion/panelcontrolestadocompra.html")
def punitario (request):
    return render(request, "aplicacion/punitario.html")
def registro (request):
    return render(request, "aplicacion/registro.html")
def sesion (request):
    return render(request, "aplicacion/sesion.html")
def shop (request):
    return render(request, "aplicacion/shop.html")
def thankyou (request):
    return render(request, "aplicacion/thankyou.html")

#DETALLES DE PERSONA Y PRODUCTO 


#FUNCIONES CREAR MODIFICAR Y ELIMINAR PARA PRODUCTO Y PERSONAS ##SE LE CAMBIA EL NOMBRE DE LA FUNCION POR LA PAGINA HTML , son vistas
#CREAR 
def personas(request):
 
    
    personas=Persona.objects.all()

    datos={

        "personas":personas
    }

    return render(request,'aplicacion/personas.html', datos)

def detallepersona(request,id):
     #persona=Persona.objects.get(rut=id)
     persona=get_object_or_404(Persona, rut=id)
     datos={
         "persona":persona
     }
     return render(request,'appcrud/detallepersona.html', datos)
 
def crearpersona(request):
    form=PersonaForm()
    
    if request.method=="POST":
        form=PersonaForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to="personas")
    
    datos={
        "form":form
    }
    return render(request, 'aplicacion/crearpersona.html', datos)

def crearproducto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('productos') 
    else:
        form = ProductoForm()

    datos = {
        'form': form
    }
    return render(request, 'aplicacion/crearproducto.html', datos)

#MODIFICAR, VER CRUD DEL PROFE Y TERMINAR BIEN NUESTROS MODIFICAR 
def modificarpersona(request, id): #*****
    persona=get_object_or_404(Persona,rut=id) #***********

    form=UpdatePersonaForm(instance=persona)
    datos={
        "form":form,
        "persona":persona
    }

    if request.method=="POST":
        form=UpdatePersonaForm(data=request.POST, files=request.FILES, instance=persona)
        if form.is_valid():
            form.save()
            return redirect(to="personas")
        
    return render(request,'aplicacion/modificarpersona.html',datos)

def modificarproducto(request, id): #******
    producto=get_object_or_404(Producto, cod_producto=id) #**********

    form=UpdateProductoForm(instance=producto)
    datos={
        "form":form,
        "producto":producto
    }

    if request.method=="POST":
        form=UpdateProductoForm(data=request.POST, files=request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect(to="productos")
        
    return render(request,'aplicacion/modificarproducto.html',datos)

#ELIMINAR , VER EL CRUD DEL PROFE Y ADAPTARLO A NUESTRA PAGINA
def eliminarpersona(request, id):
    persona = get_object_or_404(Persona, cod_persona=id) 

    datos = {
        "persona": persona
    }

    if request.method == "POST":
        persona.delete()
        return redirect(to="personas")

    return render(request, 'aplicacion/eliminarpersona.html', datos)


def eliminarproducto(request, id):
    producto = get_object_or_404(Producto, cod_producto=id)  

    if request.method == "POST":
        producto.delete()
        return redirect('productos')  

    datos = {
        "producto": producto
    }

    return render(request, 'aplicacion/eliminarproducto.html', datos)
   
def alguna_vista(request):
    persona_id = 1 
    return redirect('modificar_persona', id=persona_id)

def modificarpersona(request, id):
    persona = get_object_or_404(Persona, cod_persona=id)

    form = UpdatePersonaForm(instance=persona)
    datos = {
        "form": form,
        "persona": persona
    }

    if request.method == "POST":
        form = UpdatePersonaForm(data=request.POST, files=request.FILES, instance=persona)
        if form.is_valid():
            form.save()
            return redirect(to="personas")

    return render(request, 'aplicacion/modificarpersona.html', datos)

def modificar_persona(request, id):
    persona = get_object_or_404(Persona, cod_persona=id)

    form = UpdatePersonaForm(instance=persona)
    datos = {
        "form": form,
        "persona": persona
    }

    if request.method == "POST":
        form = UpdatePersonaForm(data=request.POST, files=request.FILES, instance=persona)
        if form.is_valid():
            form.save()
            return redirect(to="personas")

    return render(request, 'aplicacion/modificarpersona.html', datos)

def productos(request):
 
    
    productos=Producto.objects.all()

    datos={

        "productos":productos
    }

    return render(request,'aplicacion/productos.html', datos)

def orden_estado(request, idcompra):
     Envio = get_object_or_404(Envio, idcompra=idcompra)
     datos = {
        "Envio": Envio
    }
     return render(request, 'aplicacion/estado.html', datos)