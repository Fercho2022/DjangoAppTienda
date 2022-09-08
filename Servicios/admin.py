from django.contrib import admin
from Servicios.models import Servicio

# Register your models here.


class ServicioAdmin(admin.ModelAdmin):

    readonly_fields=('created', 'updated')    # con esta instrucción de solo lectura hago que los campos created y updated se reflejen en el panel de administración


admin.site.register(Servicio, ServicioAdmin) # con esta instruccón se registra el modelo en el panel de administración
