
from django.urls import path, include
from .views import index, beretta, camisa, carpa, casco, chaleco, cuchillo, pantalon, valken, about, admini, cart, checkout, estado
from .views import miscompras, panelcerrarsesion, panelcontrol, panelcontrolagregararmas,panelcontroleditararmas, panelcontrolestadocompra
from .views import panelcontrolusuarios, punitario, registro, sesion, shop, thankyou
from . import views

#PARA TRABAJAR CON IMAGENES
from django.conf import settings
from django.conf.urls.static import static

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
       path('admini/', admini, name='admini'),
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
]

#si, no me acuerdo pq va esto pero si.
if settings.DEBUG:
       urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)