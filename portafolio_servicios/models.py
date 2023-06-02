from django.db import models
from optica.models import *

# Create your models here.

class Actor(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=100, null=True)
    edad = models.IntegerField(default=18)
    tipo = models.CharField(max_length=100, null=True)
    descripcion = models.TextField(default='Descripción predeterminada')
    optica = models.ForeignKey(OpticaSolyGafas, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.nombre

class LineaNegocio(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=100, null=True)
    descripcion = models.TextField(null=True)
    optica = models.ForeignKey(OpticaSolyGafas, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.nombre

class ServicioNegocio(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=100, null=True)
    descripcion = models.TextField(null=True)
    optica = models.ForeignKey(OpticaSolyGafas, on_delete=models.SET_NULL, blank=True, null=True)
    linea = models.ForeignKey(LineaNegocio, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.nombre


class ServicioActor(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.SET_NULL, blank=True, null=True)
    servicio = models.ForeignKey(ServicioNegocio, on_delete=models.SET_NULL, blank=True, null=True)


class ObjetoNegocio(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=100, null=True)
    tipo = models.CharField(max_length=100, null=True)
    servicio = models.ForeignKey(ServicioNegocio, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.nombre