
from django.urls import path, include
from .views import index, about, admini, cart, checkout, estado
from .views import miscompras, panelcerrarsesion, panelcontrol, panelcontrolestadocompra, comprar
from .views import  punitario, crearcuenta, shop, thankyou, personas, crearpersona, modificarpersona, modificarproducto, eliminarpersona, productos, eliminarproducto, crearproducto #sesion
from . import views

#PARA TRABAJAR CON IMAGENES
from django.conf import settings
from django.conf.urls.static import static

#URLS DE APLICACION
urlpatterns = [
       path('', index, name='index'),
       path('about/', about, name='about'),
       path('admini/', admini, name='admini'),
       path('cart/', cart, name='cart'),
       path('checkout/', checkout, name='checkout'),
       path('estado/', estado, name='estado'),
       path('miscompras/', miscompras, name='miscompras'),
       path('panelcerrarsesion/', panelcerrarsesion, name='panelcerrarsesion'),
       path('panelcontrol/', panelcontrol, name='panelcontrol'),
       path('panelcontrolestadocompra/', panelcontrolestadocompra, name='panelcontrolestadocompra'),
       path('punitario/', punitario, name='punitario'),
       path('crearcuenta/', crearcuenta, name='crearcuenta'),
       #path('sesion/', sesion, name='sesion'),
       path('shop/', shop, name='shop'),
       path('thankyou/', thankyou, name='thankyou'),
       path('personas/', personas, name= 'personas'),
       path('crearpersona/', crearpersona, name= 'crearpersona'),
       path('modificarpersona/<int:id>', views.modificarpersona, name= 'modificarpersona'),
       path('eliminarpersona/', eliminarpersona, name= 'eliminarpersona' ),
       path('modificarpersona/<int:id>/', views.modificar_persona, name='modificarpersona'),
       path('alguna_vista/', views.alguna_vista, name='alguna_vista'),
       path('modificarpersona/<int:id>/', views.modificar_persona, name='modificar_persona'),
       path('eliminarpersona/<int:id>/', views.eliminarpersona, name='eliminarpersona'),
       path('productos/', productos, name = 'productos'),
       path('eliminarproducto/<int:id>/', eliminarproducto, name= 'eliminarproducto' ),
       path('crearproducto/', crearproducto, name= 'crearproducto'),
       path('modificarproducto/<int:id>/', views.modificarproducto, name='modificarproducto'),
       path('panel-control/', views.panel_control, name='panel_control'),
       path('comprar/<int:id>/', views.comprar, name='comprar'), #para comprar
       path('eliminar-carrito/<int:id>/', views.eliminar_carrito, name='eliminar_carrito'), #para eliminar del carro carrito en especifico
       

       #Esto es experimental, se puede sacar
]

#si, no me acuerdo pq va esto pero si.
if settings.DEBUG:
       urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)