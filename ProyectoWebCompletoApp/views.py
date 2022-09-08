from django.shortcuts import render, HttpResponse
from Servicios.models import Servicio        # importo la clase Servicio del models de la aplicación Servicios ya que necesito los objetos creados con el panel de administración

# Create your views here.

def home(request):

    return render (request, "ProyectoWebCompletoApp/home.html")







def blog(request):

    return render (request, "ProyectoWebCompletoApp/blog.html")

