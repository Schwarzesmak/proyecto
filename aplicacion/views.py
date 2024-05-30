from django.shortcuts import render

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
def admin (request):
    return render(request, "aplicacion/admin.html")
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

