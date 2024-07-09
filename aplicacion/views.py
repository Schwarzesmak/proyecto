from django.shortcuts import get_list_or_404, render, get_object_or_404, redirect
from django.utils import timezone #para importar la hora , es para el carro y su envio
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
#desde el crud del profe
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages 
from .models import Persona, Producto, Envio, Pedido,Carrito ,Usuario, DetallePedido
from os import path, remove 
from django.conf import settings
#Cosas que importe en esta rama
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
#importar forms.py tambien, falta
from .forms import PersonaForm, UpdatePersonaForm, ProductoForm, UpdateProductoForm, CrearCuentaForm, UpdateUsuarioForm, UsuarioForm #para formularios de persona y productos


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

#Funcion de logout
def salir(request):
    logout(request)
    return redirect(to='index')

def about (request):
    return render(request, "aplicacion/about.html")

# Si el usuario envía un formulario POST con un nombre de usuario y contraseña válidos para un usuario administrador, 
# se inicia sesión y se redirige al panel de control. Si no, muestra un mensaje de error en la página admini.html.
def admini(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('panelcontrol')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    return render(request, "aplicacion/admini.html")

def is_admin(user):
    return user.is_authenticated and user.is_staff

from django.shortcuts import render, get_object_or_404, redirect
from .models import Carrito, Usuario


#Se maneja el carrito, con permisos de inicio de sesion, muestra los productos en carro y calcula subtotal
@login_required
def cart(request):
    user = request.user
    usr = get_object_or_404(Usuario, nombusuario=user)
    carritos = Carrito.objects.filter(usuario_id=usr)
    productos = Producto.objects.all()
    subtotal = sum(c.get_total_price() for c in carritos)

    datos = {
        "carritos": carritos,
        "productos": productos,
        "subtotal": subtotal,
    }

    print("Y aqui")  # Confirmar que se accede a la vista

    if request.method == 'POST':
        print("Pasa por aca?")  # Confirmar que se recibe una solicitud POST
        id = request.POST.get('id')  # Obtener el ID del carrito a eliminar
        print(f"Carrito ID: {id}")  # Confirmar el ID del carrito
        
        carrito = get_object_or_404(Carrito, id=id, usuario=usr)
        carrito.delete()  # Eliminar el carrito

        #Recalcular subtotal después de eliminar el producto
        carritos = Carrito.objects.filter(usuario=usr)
        subtotal = sum(c.get_total_price() for c in carritos)
        datos['carritos'] = carritos
        datos['subtotal'] = subtotal

        # Redirigir nuevamente a la página de carrito después de eliminar
        return redirect('cart')

    return render(request, "aplicacion/cart.html", datos)

#Elimina un producto específico basado en su ID cod_producto
@user_passes_test(is_admin)
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
# permite eliminar un carrito de compras específico para el usuario autenticado. 
@login_required
def eliminar_carrito(request, id):
    if request.method == 'POST':
        carrito_id = id
        carrito = get_object_or_404(Carrito, id=carrito_id, usuario=request.user.usuario)
        carrito.delete()
        print(f'Carrito eliminado correctamente: {carrito_id}')
        return redirect('cart')
    else:
        print(f'No se recibió una solicitud POST para eliminar el carrito con ID: {id}')
        return redirect('cart')  
    
    
# Si la solicitud es POST, recupera y muestra el subtotal del carrito
def checkout (request):
    
    if request.method == 'POST':
        print(f'Solicitud POST recibida para eliminar el carrito con ID: {id}')
        subtotal = request.POST.get('subtotal', 0)  # Recuperar el subtotal del formulario
        print(f'Carrito con ID {id} eliminado exitosamente.')
        return render(request, 'aplicacion/checkout.html', {'subtotal': subtotal})
    
    return render(request, 'aplicacion/checkout.html')
# muestra el estado de los pedidos realizados por el usuario autenticado. Obtiene los pedidos y detalles de pedidos asociados al usuario
@login_required
def estado (request):
    #obtener el carro del usuario en especifico
    user = request.user
    usr = get_object_or_404(Usuario, nombusuario=user) 
    pedidos_usuario = Pedido.objects.filter(usuario_id=usr)
    pedidos = Pedido.objects.filter(usuario_id=usr)
    detallepedido= DetallePedido.objects.all()
    datos = {
        'pedidos': pedidos,
        'detallepedido': detallepedido,
    }
    return render(request, "aplicacion/estado.html",datos)

# Muestra los detalles de un pedido específico
def detallepedido(request,id):
    detallepedido = get_list_or_404(DetallePedido, pedido_id=id)
    datos = {
        'detallepedido':detallepedido   
    }
    return render(request, "aplicacion/detallepedido.html",datos)


# Muestra los pedidos realizados por el usuario autenticado
@login_required
def miscompras(request):
    #obtener el carro del usuario en especifico
    user = request.user
    usr = get_object_or_404(Usuario, nombusuario=user) 
    pedidos = Pedido.objects.filter(usuario_id=usr)
    datos = {
        'pedidos': pedidos,
        'detallepedido': detallepedido,
    }

    return render(request, "aplicacion/miscompras.html", datos)

def panelcerrarsesion (request):
    return render(request, "aplicacion/panelcerrarsesion.html")

# Muestra el panel de control, pero solo para usuarios administradores 
@user_passes_test(is_admin)
def panelcontrol(request):
    print("Holis")
    if not request.user.is_staff:
        print("pasa por aqui??")
        messages.error(request, 'Acceso denegado. Debes ser administrador para acceder a esta página.')
        return redirect('index')  

    return render(request, "aplicacion/panelcontrol.html")


# Muestra el estado de todas las compras en el panel de control para administradores. 
@user_passes_test(is_admin) 
def panelcontrolestadocompra (request):
    pedidos=Pedido.objects.all()
    datos={

        "pedidos":pedidos
    }
    return render(request, "aplicacion/panelcontrolestadocompra.html", datos)


@user_passes_test(is_admin) 
def panelcontrolestadocompra(request):
    if not request.user.is_staff:
        messages.error(request, 'Acceso denegado. Debes ser administrador para acceder a esta página.')
        return redirect('index') 

    pedidos = Pedido.objects.all()
    datos = {
        "pedidos": pedidos
    }

    return render(request, "aplicacion/panelcontrolestadocompra.html", datos)


#Se crea un usuario, validando el usuario si existe en la base de datos, y lo crea
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
                # Guarda el usuario en la tabla User de Django
                usuario_django = form.save()
                
                # Crea la instancia de Usuario y guardarla en la tabla Usuario
                usuario_personalizado = Usuario(nombusuario=usuario_django.username, pwd=usuario_django.password)
                usuario_personalizado.save()
                
                return redirect(to="login")
            datos = {
                "form": form
            }
    return render(request, "registration/crearcuenta.html", datos)

#  muestra todos los productos disponibles en la tienda
def shop (request):
    
    productos=Producto.objects.all()

    datos={

        "productos":productos
    }
    
    return render(request, "aplicacion/shop.html", datos)

#permite a los usuarios autenticados agregar productos al carrito de compras
@login_required
def comprar(request, id):
    print("Request method:", request.method)
    producto = get_object_or_404(Producto, cod_producto=id)
    
    if request.method == 'POST' and 'add-to-cart' in request.POST:
        print("Form submitted")
        usuario = Usuario.objects.get(nombusuario=request.user.username)
        envio = Envio.objects.first()
        carrito = Carrito(usuario=usuario, envio=envio, producto=producto, cantidad=1)
        carrito.save()
        return redirect('cart')
    
    datos = {
        "producto": producto
    }
    
    return render(request, "aplicacion/comprar.html", datos)


#maneja el proceso después de que el usuario ha realizado un pedido. Verifica la solicitud y crea un nuevo Pedido con los detalles del pedido
@login_required
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
        nombre_cliente = primer_nombre + (' ' + segundo_nombre if segundo_nombre else '') + ' ' + apellido

        
        try:
            user = request.user
            usr = get_object_or_404(Usuario, nombusuario=user) 
            # Crear el pedido en la base de datos
            Pedido.objects.create(
                usuario = usr,
                nombre_cliente=nombre_cliente,
                direccion=direccion,
                correo=correo,
                celular=celular,
                region=region,
                adicional=adicional,  
                fecha_pedido=timezone.now(),  # Usar la fecha y hora actual
                estado='en_proceso'  # Estado inicial del pedido
            )
            #obtener el carro del usuario en especifico
            user = request.user
            usr = get_object_or_404(Usuario, nombusuario=user) 
            carritos_usuario = Carrito.objects.filter(usuario_id=usr)
            print(carritos_usuario)
            
            #obtener el ultimo id
            ultimo_pedido = Pedido.objects.latest('id')
            ultimo_id_pedido = ultimo_pedido.id
            
            for carrito in carritos_usuario:
                    detalle_pedido = DetallePedido.objects.create(
                        pedido= ultimo_pedido,
                        producto=carrito.producto,
                        cantidad=carrito.cantidad
                    )
                    carrito.delete()

        except Exception as e:
            # Manejar cualquier error que ocurra al crear el pedido o detalles de pedido
            # Por ejemplo, puedes agregar registro de errores, mostrar un mensaje de error, etc.
            print(f"Error al procesar pedido: {str(e)}")
            # Redirigir a una página de error o mostrar un mensaje al usuario
            return redirect('index')  

    # Si la solicitud no es POST, manejar adecuadamente
    return render(request, "aplicacion/thankyou.html")

#DETALLES DE PERSONA Y PRODUCTO 
#FUNCIONES CREAR MODIFICAR Y ELIMINAR PARA PRODUCTO Y PERSONAS ##SE LE CAMBIA EL NOMBRE DE LA FUNCION POR LA PAGINA HTML , son vistas
#muestra todos los usuarios
@user_passes_test(is_admin)
def personas(request):
 
    
    usuarios=Usuario.objects.all()

    datos={

        "usuarios":usuarios
    }

    return render(request,'aplicacion/personas.html', datos)

# muestra un formulario para crear nuevos usuarios y también crea un usuario correspondiente en auth.User de Django. Si es válido, guarda los usuarios y redirige a la lista de personas. 
@user_passes_test(is_admin)
def crearpersona(request):
    form=UsuarioForm()
    
    if request.method=="POST":
        form=UsuarioForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()

            # Crea un usuario de Django usando los mismos datos
            nombusuario = form.cleaned_data['nombusuario'] 
            pwd = form.cleaned_data['pwd'] 
            
            # Crea el usuario de Django
            user_django = User.objects.create_user(username=nombusuario, password=pwd)
            
            # Guarda el usuario de Django
            user_django.save()

            messages.success(request, 'Persona agregada al registro')
            return redirect(to="personas")
    
    datos={
        "form":form
    }
    return render(request, 'aplicacion/crearpersona.html', datos)

#permite a los administradores agregar nuevos productos mediante el formulario
@user_passes_test(is_admin)
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

#Permite modificar los datos de un usuario específico, actualizando los datos en la bd
def modificarpersona(request, id):
    usuario = get_object_or_404(Usuario, nombusuario=id)

    form = UpdateUsuarioForm(instance=usuario)
    datos = {
        "form": form,
        "usuario": usuario
    }

    if request.method == "POST":
        form = UpdateUsuarioForm(data=request.POST, files=request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
            messages.warning(request, 'Pesona Modificada')
            return redirect(to="personas")

    return render(request, 'aplicacion/modificarpersona.html', datos)

# Permite modificar los datos de un producto específico, actualizando en la bd
@user_passes_test(is_admin)
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


#Permite eliminar un usuario específico
def eliminarpersona(request, id):
    usuario = get_object_or_404(Usuario, nombusuario=id)

    datos = {
        "usuario": usuario
    }

    if request.method == "POST":
        # Eliminar el usuario de auth.User
        user_to_delete = User.objects.get(username=usuario.nombusuario)
        user_to_delete.delete()

        # Eliminar el usuario de tu modelo Usuario
        usuario.delete()
        messages.success(request, 'Usuario eliminado exitosamente')
        return redirect('personas')

    return render(request, 'aplicacion/eliminarpersona.html', datos)
# Permite eliminar un producto especifico, verificando si esta en la bd, y eliminarlo desde ahi
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

# Permite modificar los datos de una persona específica
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
#muestra todos los producto del cliente, solo vista de administrador
@user_passes_test(is_admin)
def productos(request):
    productos=Producto.objects.all()

    datos={

        "productos":productos
    }

    return render(request,'aplicacion/productos.html', datos)

#  Muestra el estado de envío de una compra que realizó el cliente
def orden_estado(request, idcompra):
     Envio = get_object_or_404(Envio, idcompra=idcompra)
     datos = {
        "Envio": Envio
    }
     return render(request, 'aplicacion/estado.html', datos)
 
 # muestra todos los pedidos ordenados por fecha de pedido descendente en la página
@user_passes_test(is_admin)
def panel_control(request):
    # Obtener todos los pedidos ordenados por fecha de pedido descendente
    pedidos = pedidos.objects.all().order_by('-fecha_pedido')
    
    context = {
        'pedidos': pedidos
    }
    
    return render(request, 'panel_control.html', context)

#devuelve un JSON con información detallada de todos los pedidos y sus productos asociados. Es útil para integraciones o consumos de API donde se necesite acceder a estos datos estructurados.
def api_pedidos(request):
    pedidos = Pedido.objects.all()
    data = []
    
    for pedido in pedidos:
        productos_pedido = pedido.productos.all() 
        
        for producto in productos_pedido:
            data.append({
                'id': pedido.id,
                'nombre_cliente': pedido.nombre_cliente,
                'fecha_pedido': pedido.fecha_pedido,
                'estado': pedido.estado,
                'nombre_producto': producto.nombre,  
                'precio_producto': producto.precio,  
            })
    return JsonResponse(data, safe=False)


#Manejan las actualizaciones del estado y la boleta de un pedido específico identificado por pedido_id.
@csrf_exempt
def actualizar_estado_pedido(request, pedido_id, nuevo_estado):
    if request.method == 'POST':
        try:
            pedido = Pedido.objects.get(id=pedido_id)
            pedido.estado = nuevo_estado
            pedido.save()
            return JsonResponse({'status': 'success'}, status=200)
        except Pedido.DoesNotExist:
            return JsonResponse({'error': 'Pedido no encontrado'}, status=404)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
def actualizar_boleta_pedido(request, pedido_id, nueva_boleta):
    if request.method == 'POST':
        try:
            pedido = Pedido.objects.get(id=pedido_id)
            pedido.boleta = nueva_boleta == 'true'
            pedido.save()
            return JsonResponse({'status': 'success'}, status=200)
        except Pedido.DoesNotExist:
            return JsonResponse({'error': 'Pedido no encontrado'}, status=404)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

#Maneja la lógica básica de inicio de sesión de usuarios utilizando las credenciales proporcionadas.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            pass
#maneja las actualizaciones del carrito de compras según la acción de subir o bajar
@require_POST

def update_cart(request):
    cart_id = request.POST.get('cart_id')
    action = request.POST.get('action')

    if cart_id and action:
        try:
            cart_item = Carrito.objects.get(id=cart_id)
            if action == 'increase':
                cart_item.cantidad += 1
            elif action == 'decrease' and cart_item.cantidad > 1:
                cart_item.cantidad -= 1
            cart_item.save()
            new_quantity = cart_item.cantidad
            return JsonResponse({'success': True, 'new_quantity': new_quantity})
        except Carrito.DoesNotExist:
            return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': False})