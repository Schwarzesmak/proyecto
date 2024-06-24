from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .enumeraciones import *
from django.contrib.auth.models import User

# Create your models here.
class Perfil(models.Model):
    usuario=models.OneToOneField(User, related_name='usuario', on_delete=models.CASCADE)
    telefono=models.CharField(max_length=9, null=False)
    direccion=models.CharField(max_length=250, null=False)

class Producto(models.Model):
    cod_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    tipo_producto = models.CharField(max_length=10, choices=TIPO_PRODUCTO, default='OTRO PRODUCTO')
    tipo_municion = models.CharField(max_length=100, choices=TIPO_MUNICION, default='OTRO')
    precio = models.IntegerField(validators=[MinValueValidator(1000), MaxValueValidator(999999999)])
    stock = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='productos', null=True)

    def __str__(self): 
        return self.nombre


class Persona (models.Model):
    cod_persona    =  models.IntegerField(primary_key=True,  validators=[MinValueValidator(1), MaxValueValidator(999999999)])
    pnombre        =  models.CharField(max_length=20, null=False)
    snombre        =  models.CharField(max_length=20, null=True)
    apellidop      =  models.CharField(max_length=20, null=False)
    apellidom      =  models.CharField(max_length=20, null=False)
    correo         =  models.EmailField(error_messages="El correo")
    direccion      =  models.CharField(max_length=50, null=False)
    celular        =  models.IntegerField(verbose_name="Fono", validators=[MinValueValidator(100000000), MaxValueValidator(999999999)])
    region         =  models.CharField(max_length=25, choices=REGIONES, default="CONCEPCION")  
    info_adicional =  models.CharField(max_length=100, null=False)
    imagen= models.ImageField(upload_to='personas',null=True)
    

class Usuario (models.Model):
    nombusuario = models.CharField(primary_key=True, max_length=20, null=False)
    pwd = models.CharField(max_length=20, null=False)
    
    
class Envio (models.Model):
    idcompra = models.AutoField(primary_key=True)
    fecha_compra = models.DateField(("Fecha de compra"), auto_now=False, auto_now_add=False)
    estado = models.CharField(max_length=100, choices=ESTADOS, default="ENTREGADO")
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    imagenenvio = models.ImageField(upload_to='imagenenvios',null=True)
    
class Carrito(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='usuario')
    envio = models.ForeignKey(Envio, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(validators=[MinValueValidator(1)])

    def get_total_price(self):
        return self.producto.precio * self.cantidad 

    def __str__(self):
        return f"Carrito de {self.usuario} - Producto: {self.producto.nombre} {self.usuario.nombusuario}"  

class Registro(models.Model): 
     usuario = models.CharField(max_length=50, primary_key=True)
     email = models.CharField(max_length=20)
     contraseña = models.CharField(max_length=18)
     

# Esto es experimental, si se requiere se saca 
class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_cliente = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    correo = models.EmailField()
    usuario = models.CharField(max_length=50)
    celular = models.CharField(max_length=20)
    region         =  models.CharField(max_length=25, choices=REGIONES, default="CONCEPCION")
    fecha_pedido = models.DateField()
    boleta = models.CharField(max_length=15, choices=[
        ('sin_boleta', 'Sin boleta'),
        ('con_boleta', 'Con boleta'),
    ])
    estado = models.CharField(max_length=20, choices=[
        ('cancelado', 'Cancelado'),
        ('en_proceso', 'En Proceso'),
        ('finalizado', 'Finalizado'),
    ], default='En proceso')
    productos = models.ManyToManyField('Producto', through='DetallePedido')
    def __str__(self):  
        return f"Pedido {self.id} - {self.nombre_cliente}"
    
class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return f"Detalle de Pedido {self.pedido.id} - Producto {self.producto.nombre}"
