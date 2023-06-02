from django.db import models
from optica.models import *

# Create your models here.

class Mision(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    descripcion = models.TextField(null=True)

    def __str__(self):
        return self.id

class Medio(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=30, null=True)
    descripcion = models.TextField(null=True)
    optica = models.ForeignKey(OpticaSolyGafas, on_delete=models.SET_NULL, blank=True, null=True)
    mision = models.ForeignKey(Mision, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.nombre


class Estrategia(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=30, null=True)
    descripcion = models.TextField(null=True)
    mision = models.ForeignKey(Mision, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.nombre

class Accion(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=30, null=True)
    descripcion = models.TextField(null=True)
    estrategia = models.ForeignKey(Estrategia, on_delete=models.SET_NULL, blank=True, null=True)
    medio = models.ForeignKey(Medio, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.nombre

class Tactica(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=30, null=True)
    descripcion = models.TextField(null=True)
    estrategia = models.ForeignKey(Estrategia, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.nombre

class Politica(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=30, null=True)
    descripcion = models.TextField(null=True)

    def __str__(self):
        return self.nombre

class Regla(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=30, null=True)
    descripcion = models.TextField(null=True)
    politica = models.ForeignKey(Politica, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.nombre

class Tactica_Regla(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    tactica = models.ForeignKey(Tactica, on_delete=models.SET_NULL, blank=True, null=True)
    regla = models.ForeignKey(Regla, on_delete=models.SET_NULL, blank=True, null=True)



## FINES
class Vision(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    descripcion = models.TextField(null=True)

    def __str__(self):
        return self.id


class Objetivos(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=30, null=True)
    descripcion = models.TextField(null=True)

    def __str__(self):
        return self.nombre


class ResultadoEsperado(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=30, null=True)
    descripcion = models.TextField(null=True)
    optica = models.OneToOneField(Objetivos, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.nombre



class Fines(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=30, null=True)
    descripcion = models.TextField(null=True)
    optica = models.ForeignKey(OpticaSolyGafas, on_delete=models.SET_NULL, blank=True, null=True)
    vision = models.ForeignKey(Vision, on_delete=models.SET_NULL, blank=True, null=True)
    resultado_esperado = models.ForeignKey(ResultadoEsperado, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.nombre

class Metas(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=30, null=True)
    descripcion = models.TextField(null=True)
    vision = models.ForeignKey(Vision, on_delete=models.SET_NULL, blank=True, null=True)
    resultado_esperado = models.ForeignKey(ResultadoEsperado, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.nombre