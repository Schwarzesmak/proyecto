
from django.urls import path
from .views import index, beretta, camisa, carpa, casco, chaleco, cuchillo, pantalon, valken, about, admin, cart, checkout, estado
from .views import miscompras, panelcerrarsesion, panelcontrol, panelcontrolagregararmas,panelcontroleditararmas, panelcontrolestadocompra
from .views import panelcontrolusuarios, punitario, registro, sesion, shop, thankyou

#URLS DE APLICACION
urlpatterns = [
       path('', index, name='index'),
       path('producto/beretta', beretta, name='beretta'),
       path('producto/camisa', camisa, name='camisa'),
       path('producto/carpa', carpa, name='carpa'),
       path('producto/casco', casco, name='casco'),
       path('producto/chaleco', chaleco, name='chaleco'),
       path('producto/cuchillo', cuchillo, name='cuchillo'),
       path('producto/pantalon', pantalon, name='pantalon'),
       path('producto/valken', valken, name='valken'),
       path('about/', about, name='about'),
       path('admin/', admin, name='admin'),
       path('cart/', cart, name='cart'),
       path('checkout/', checkout, name='checkout'),
       path('estado/', estado, name='estado'),
       path('miscompras/', miscompras, name='miscompras'),
       path('panelcerrarsesion/', panelcerrarsesion, name='panelcerrarsesion'),
       path('panelcontrol/', panelcontrol, name='panelcontrol'),
       path('panelcontrolagregararmas/', panelcontrolagregararmas, name='panelcontrolagregararmas'),
       path('panelcontroleditararmas/', panelcontroleditararmas, name='panelcontroleditararmas'),
       path('panelcontrolestadocompra/', panelcontrolestadocompra, name='panelcontrolestadocompra'),
       path('panelcontrolusuarios/', panelcontrolusuarios, name='panelcontrolusuarios'),
       path('punitario/', punitario, name='punitario'),
       path('registro/', registro, name='registro'),
       path('sesion/', sesion, name='sesion'),
       path('shop/', shop, name='shop'),
       path('thankyou/', thankyou, name='thankyou'),
       #Esto es experimental, se puede sacar
       path('', views.home, name='home'),
       path('estado_compra/', views.estado_compra, name='estado_compra'),
       path('usuarios/', views.usuarios, name='usuarios'),
       path('agregar_productos/', views.agregar_productos, name='agregar_productos'),
       path('editar_producto/', views.editar_producto, name='editar_producto'),
       path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
]
