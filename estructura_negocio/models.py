from django.db import models
from optica.models import *

# Create your models here.

class Componente(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=100, null=True)
    descripcion = models.TextField(null=True)
    optica = models.ForeignKey(OpticaSolyGafas, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.nombre


class Canal(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=100, null=True)
    tipo = models.CharField(max_length=50, null=True)
    componente = models.ForeignKey(Componente, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.nombre

class Actividad(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=100, null=True)
    descripcion = models.TextField(null=True)
    canal = models.ForeignKey(Canal, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.nombre


class Participante(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=100, null=True)
    descripcion = models.TextField(null=True)
    optica = models.ForeignKey(OpticaSolyGafas, on_delete=models.SET_NULL, blank=True, null=True)
    actividad = models.ForeignKey(Actividad, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.nombre

class Recurso(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=100, null=True)
    optica = models.ForeignKey(OpticaSolyGafas, on_delete=models.SET_NULL, blank=True, null=True)
    actividad = models.ForeignKey(Actividad, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.nombre
