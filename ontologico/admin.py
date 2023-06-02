from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(Rol)
admin.site.register(Persona)
admin.site.register(Capacitacion)
admin.site.register(Capacitacion_Persona)
admin.site.register(Maquina)
admin.site.register(Maquina_Persona)
admin.site.register(Proveedores)
admin.site.register(Proveedores_Optica)
admin.site.register(Servicio)
admin.site.register(Servicio_Optica)
admin.site.register(Servicio_Persona)
admin.site.register(Persona_Optica)
admin.site.register(Compra)
admin.site.register(Producto)
admin.site.register(Producto_Compra)