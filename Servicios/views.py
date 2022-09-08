from django.shortcuts import render
from .models import Servicio  

# Create your views here.




def servicios(request):

    servicios=Servicio.objects.all()   # guardo dentro de servicios todos los objetos Servicio creados desde el panel de administración

    return render (request, "Servicios/servicios.html", {"servicios":servicios})