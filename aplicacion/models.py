from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .enumeraciones import *

# Create your models here.
TIPO_MUNICION={
    ("POSTON", "Poston"), 
    ("AIRSOFT", "Airsoft"),
    ("BALIN", "Balin"),
    ("OTRO", "Otro"),
}

TIPO_PRODUCTO={
    ("ROPA", "Ropa"),
    ("ARMA", "Arma"),
    ("CUCHILLA", "Cuchilla"),
}

class Producto(models.Model):
    nombre = models.CharField(primary_key=True, max_length=50, null=False)
    tipo_producto = models.CharField(max_length=10, choices=TIPO_PRODUCTO, default="OTRO PRODUCTO")
    #ESTO VA EN HTML, TIPO_MUNICION
    tipo_municion = models.CharField(max_length=100, choices=TIPO_MUNICION, default= "OTRO")
    precio = models.IntegerField(verbose_name='Dinero', validators=[MinValueValidator(1000), MaxValueValidator(999999999)])
    stock = models.IntegerField( validators=[MinValueValidator(0)], default=0 )
    imagen=models.ImageField(upload_to='productos',null=True)
    
    def __str__(self):
        return self.nombre


class Persona (models.Model):
    pnombre        =  models.CharField(primary_key=True, max_length=20, null=False)
    snombre        =  models.CharField(max_length=20, null=True)
    apellidop      =  models.CharField(max_length=20, null=False)
    apellidom      =  models.CharField(max_length=20, null=False)
    correo         =  models.EmailField(error_messages="El correo maldito Peruano")
    direccion      =  models.CharField(max_length=50, null=False)
    celular        =  models.IntegerField(verbose_name="Fono", validators=[MinValueValidator(100000000), MaxValueValidator(999999999)])
    region         =  models.CharField(max_length=25, choices=REGIONES, default="CONCEPCION")  
    info_adicional =  models.CharField(max_length=100, null=False)
    imagen=models.ImageField(upload_to='personas',null=True)
    

class Usuario (models.Model):
    nombusuario = models.CharField(primary_key=True, max_length=20, null=False)
    pwd = models.CharField(max_length=20, null=False)
    
    
class Envio (models.Model):
    idcompra = models.AutoField(primary_key=True)
    fecha_compra = models.DateField(("Fecha de compra"), auto_now=False, auto_now_add=False)
    estado = models.CharField(max_length=100, choices=ESTADOS, default="ENTREGADO")
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    imagenenvio = models.ImageField(upload_to='imagenenvios',null=True)
    
