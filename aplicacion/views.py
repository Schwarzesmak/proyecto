from django.shortcuts import render
#desde el crud del profe
from django.shortcuts import get_object_or_404, redirect
from .models import Persona, Producto #Carrito, Usuario, Envio
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
def panelcontrolagregararmas (request):
    return render(request, "aplicacion/panelcontrolagregararmas.html")
def panelcontroleditararmas (request):
    return render(request, "aplicacion/panelcontroleditararmas.html")
def panelcontrolestadocompra (request):
    return render(request, "aplicacion/panelcontrolestadocompra.html")
def panelcontrolusuarios (request):
    return render(request, "aplicacion/panelcontrolusuarios.html")
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
    form=ProductoForm()
    
    if request.method=="POST":
        form=ProductoForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to="#NOMBRE_PAG_HTML_AQUI!!!")
    
    datos={
        "form":form
    }
    return render(request, 'aplicacion/#NOMBRE_PAG_HTML_AQUI!!!', datos)

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
    producto=get_object_or_404(Producto,rut=id) #**********

    form=UpdateProductoForm(instance=producto)
    datos={
        "form":form,
        "producto":producto
    }

    if request.method=="POST":
        form=UpdateProductoForm(data=request.POST, files=request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect(to="#NOMBRE_PAG_HTML_AQUI!!!")
        
    return render(request,'aplicacion/#NOMBRE_PAG_HTML_AQUI!!!',datos)

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
    producto=get_object_or_404(Producto,rut=id) 

    datos={
        "producto":producto
    }

    if request.method=="POST":
        producto.delete()
        return redirect(to="#NOMBRE_PAG_HTML_AQUI!!!")
   
def alguna_vista(request):
    persona_id = 1  # Aquí debes obtener el id de la persona que deseas modificar
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
