from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone #para importar la hora , es para el carro y su envio
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
#desde el crud del profe
from django.contrib.auth.models import User
from django.contrib import messages 
from .models import Persona, Producto, Envio, Pedido,Carrito ,Usuario, DetallePedido
from os import path, remove 
from django.conf import settings
#importar forms.py tambien, falta
from .forms import PersonaForm, UpdatePersonaForm, ProductoForm, UpdateProductoForm, CrearCuentaForm #para formularios de persona y productos


# Create your views here.
#Aqui es para las  paginas
def index (request):
    
    #obtener productos en especifico, beretta, cuchillo y carpa    
    beretta = Producto.objects.get(nombre="Beretta")
    cuchillo = Producto.objects.get(nombre="cuchillo")
    carpa = Producto.objects.get(nombre="carpa")
    
    datos={

        "cuchillo":cuchillo,
        "beretta":beretta,
        "carpa":carpa
    }
    
    return render(request, "aplicacion/index.html", datos)



def beretta(request):
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

def about (request):
    return render(request, "aplicacion/about.html")
def admini (request):
    return render(request, "aplicacion/admini.html")

@login_required
def cart(request):
    user = request.user
    usr = get_object_or_404(Usuario, nombusuario=user) 
    carritos = Carrito.objects.filter(usuario_id=usr)
    productos = Producto.objects.all()

    # Calcular subtotal del carrito
    subtotal = sum(c.get_total_price() for c in carritos)

    datos = {
        "carritos": carritos,
        "productos": productos,
        "subtotal": subtotal,  # Pasamos el subtotal al contexto
    }

    return render(request, "aplicacion/cart.html", datos)

#vista para eliminar carro 
def eliminar_carrito(request, id):
    carrito = get_object_or_404(Carrito, id=id)
    
    if request.method == 'POST':
        carrito.delete()
        return redirect('cart')  # Redirigir a la página del carrito después de eliminar
    
    return redirect('cart')  # Manejar casos donde no sea un POST (opcional dependiendo de la lógica de tu aplicación)


def checkout (request):
    
    if request.method == 'POST':
        subtotal = request.POST.get('subtotal', 0)  # Recuperar el subtotal del formulario

        # Aquí puedes realizar cualquier lógica adicional, como procesar el pedido, aplicar cupones, etc.

        return render(request, 'aplicacion/checkout.html', {'subtotal': subtotal})

    # Si el método no es POST (por ejemplo, GET), puedes manejarlo según tu flujo de aplicación
    return render(request, 'aplicacion/checkout.html')
def estado (request):
    
    estados=Carrito.objects.all()
    envios = Envio.objects.all()

    datos={

        "estados":estados,
        "envios":envios
    }
    return render(request, "aplicacion/estado.html",datos)

def miscompras(request):
    pedidos = Pedido.objects.all()
    detallepedido= DetallePedido.objects.all()
    datos = {
        'pedidos': pedidos,
        'detallepedido': detallepedido,
    }

    return render(request, "aplicacion/miscompras.html", datos)

def panelcerrarsesion (request):
    return render(request, "aplicacion/panelcerrarsesion.html")
def panelcontrol (request):
    return render(request, "aplicacion/panelcontrol.html")
#para que se vean los pedidos en panel control estado 
def panelcontrolestadocompra (request):
    pedidos=Pedido.objects.all()
    datos={

        "pedidos":pedidos
    }
    return render(request, "aplicacion/panelcontrolestadocompra.html", datos)
def punitario (request):
    return render(request, "aplicacion/punitario.html")

def crearcuenta (request):
    form=CrearCuentaForm()
    datos={
        "form":form
    }
    if request.method=="POST":
        form=CrearCuentaForm(data=request.POST)
        usr=request.POST["username"]
        existe=User.objects.filter(username=usr).exists()
        if existe:
            alerta="El usuario ya existe"
            datos={
                "form":form,
                "alerta":alerta
            }
        else:
            if form.is_valid():
                form.save()
                return redirect(to="login")
            datos={
                "form":form
            }
    return render(request, "registration/crearcuenta.html", datos)

#def sesion (request):
#    return render(request, "aplicacion/sesion.html")

def shop (request):
    
    productos=Producto.objects.all()

    datos={

        "productos":productos
    }
    
    return render(request, "aplicacion/shop.html", datos)

@login_required
def comprar(request, id):
    producto = get_object_or_404(Producto, cod_producto=id)
    
    if request.method == 'POST' and 'add-to-cart' in request.POST:
        # Recuperar el usuario actual
        usuario = Usuario.objects.get(nombusuario=request.user.username)
        
        # Aquí asume que tienes algún método para obtener el envío correspondiente
        # Puedes ajustar esto según cómo manejas los envíos en tu sistema
        envio = Envio.objects.first()  # Ajusta esta lógica según corresponda

        # Crear un nuevo objeto Carrito y guardarlo en la base de datos
        carrito = Carrito(usuario=usuario, envio=envio, producto=producto, cantidad=1)
        carrito.save()
        
        # Redirigir a la página del carrito o a donde desees después de añadir al carrito
        return redirect('cart')
    
    datos = {
        "producto": producto
    }
    
    return render(request, "aplicacion/comprar.html", datos)

@require_POST
def thankyou(request):
    # Verificar si la solicitud es POST (idealmente, deberías manejar otros métodos también)
    if request.method == 'POST':
        # Recuperar los datos del formulario
        primer_nombre = request.POST.get('primer_nombre', '')
        segundo_nombre = request.POST.get('segundo_nombre', '')
        apellido = request.POST.get('apellido', '')
        direccion = request.POST.get('direccion', '')
        correo = request.POST.get('correo', '')
        celular = request.POST.get('celular', '')
        region = request.POST.get('region', '')
        adicional = request.POST.get('adicional', '')

        # Concatenar nombres si es necesario
        nombre_cliente = primer_nombre + (' ' + segundo_nombre if segundo_nombre else '') + ' ' + apellido

        try:
            # Crear el pedido en la base de datos
            pedido = Pedido.objects.create(
                nombre_cliente=nombre_cliente,
                direccion=direccion,
                correo=correo,
                celular=celular,
                region=region,
                adicional=adicional,  # Incluir el campo adicional en la creación del pedido
                fecha_pedido=timezone.now(),  # Usar la fecha y hora actual
                estado='en_proceso'  # Estado inicial del pedido
            )

            # Ejemplo de cómo agregar detalles de pedido (puedes ajustar según tu modelo)
            # Esto es solo un ejemplo, ajusta según tus modelos de datos y cómo manejas el carrito
            productos_en_carrito = request.session.get('carrito', {})  # Obtener productos del carrito desde la sesión

            for producto_id, cantidad in productos_en_carrito.items():
                producto = Producto.objects.get(pk=producto_id)
                DetallePedido.objects.create(
                    pedido=pedido,
                    producto=producto,
                    cantidad=cantidad
                )

            # Limpiar carrito en la sesión después de completar el pedido
            del request.session['carrito']

            # Redirigir a una página de confirmación o de gracias
            return redirect('confirmacion_pedido')  # Ajusta el nombre de la URL según tu configuración

        except Exception as e:
            # Manejar cualquier error que ocurra al crear el pedido o detalles de pedido
            # Por ejemplo, puedes agregar registro de errores, mostrar un mensaje de error, etc.
            print(f"Error al procesar pedido: {str(e)}")
            # Redirigir a una página de error o mostrar un mensaje al usuario
            return redirect('index')  # Ajusta el nombre de la URL según tu configuración

    # Si la solicitud no es POST, manejar adecuadamente (idealmente deberías manejar otros métodos también)
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

#def detallepersona(request,id):
     #persona=Persona.objects.get(rut=id)
#     persona=get_object_or_404(Persona, rut=id)
#     datos={
#         "persona":persona
#     }
#     return render(request,'appcrud/detallepersona.html', datos)
 
def crearpersona(request):
    form=PersonaForm()
    
    if request.method=="POST":
        form=PersonaForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Persona agregada al registro')
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
            messages.success(request, 'Persona Agregada')
            return redirect('productos') 
    else:
        form = ProductoForm()

    datos = {
        'form': form
    }
    return render(request, 'aplicacion/crearproducto.html', datos)

#MODIFICAR, VER CRUD DEL PROFE Y TERMINAR BIEN NUESTROS MODIFICAR 
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
            messages.warning(request, 'Pesona Modificada')
            return redirect(to="personas")

    return render(request, 'aplicacion/modificarpersona.html', datos)

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
            messages.success(request, 'Producto Modificado')
            return redirect(to="productos")
        
    return render(request,'aplicacion/modificarproducto.html',datos)

#ELIMINAR , VER EL CRUD DEL PROFE Y ADAPTARLO A NUESTRA PAGINA
def eliminarpersona(request, id):
    persona = get_object_or_404(Persona, cod_persona=id) 

    datos = {
        "persona": persona
    }

    if request.method == "POST":
        if persona.imagen:
            remove(path.join(str(settings.MEDIA_ROOT).replace('/media','') + persona.imagen.url))
        persona.delete()
       #  "remove(path.join(str(settings.MEDIA_ROOT).replace('media/') persona.imagen.url))) Esto es siempre y cuando que la imagen no sirva"
        messages.error(request, 'Persona eliminada')
        return redirect(to="personas")
    return render(request, 'aplicacion/eliminarpersona.html', datos)


def eliminarproducto(request, id):
    producto = get_object_or_404(Producto, cod_producto=id)

    if request.method == "POST":
        if producto.imagen:
            remove(path.join(str(settings.MEDIA_ROOT).replace('/media','')+producto.imagen.url))
        producto.delete()
        messages.success(request, 'Producto Eliminado')
        return redirect('productos')

    datos = {
        "producto": producto
    }

    return render(request, 'aplicacion/eliminarproducto.html', datos)

#---------OTRAS VISTAS--------------------#
def alguna_vista(request):
    persona_id = 1 
    return redirect('modificar_persona', id=persona_id)

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
 
 #Esto es experimental, si se requiere se saca
def panel_control(request):
    # Obtener todos los pedidos ordenados por fecha de pedido descendente
    pedidos = pedidos.objects.all().order_by('-fecha_pedido')
    
    context = {
        'pedidos': pedidos
    }
    
    return render(request, 'panel_control.html', context)
