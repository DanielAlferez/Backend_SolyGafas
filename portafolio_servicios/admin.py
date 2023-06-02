from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(Actor)
admin.site.register(LineaNegocio)
admin.site.register(ServicioNegocio)
admin.site.register(ServicioActor)
admin.site.register(ObjetoNegocio)