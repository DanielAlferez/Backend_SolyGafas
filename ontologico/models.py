from django.db import models
from optica.models import *

# Create your models here.


class Rol(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    tipo = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.tipo


class Persona(models.Model):
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]

    id = models.AutoField(primary_key=True, editable=False)
    cedula = models.CharField(max_length=12, null=True)
    nacimiento = models.DateField(null=True)
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES, null=True)
    nombre = models.CharField(max_length=50, null=True)
    celular = models.CharField(max_length=10, null=True)
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, blank=True, null=True)
    salario = models.BigIntegerField(null=True)

    def __str__(self):
        return self.nombre

class Capacitacion(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    descripcion = models.TextField(null=True)
    fecha = models.DateField(null=True)

    def __str__(self):
        return self.fecha


class Capacitacion_Persona(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    persona = models.ForeignKey(Persona, on_delete=models.SET_NULL, blank=True, null=True)
    capacitacion = models.ForeignKey(Capacitacion, on_delete=models.SET_NULL, blank=True, null=True)


class Maquina(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=30, null=True)
    descripcion = models.TextField(null=True)

    def __str__(self):
        return self.nombre


class Maquina_Persona(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    persona = models.ForeignKey(Persona, on_delete=models.SET_NULL, blank=True, null=True)
    maquina = models.ForeignKey(Maquina, on_delete=models.SET_NULL, blank=True, null=True)


class Proveedores(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=30, null=True)
    persona = models.ForeignKey(Persona, on_delete=models.SET_NULL, blank=True, null=True)
    maquina = models.ForeignKey(Maquina, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.nombre


class Proveedores_Optica(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    proveedor = models.ForeignKey(Proveedores, on_delete=models.SET_NULL, blank=True, null=True)
    optica = models.ForeignKey(OpticaSolyGafas, on_delete=models.SET_NULL, blank=True, null=True)


class Servicio(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=30, null=True)
    fecha = models.DateField(null=True)
    resultados = models.TextField(null=True)
    encargo = models.TextField(null=True)
    maquina = models.ForeignKey(Maquina, on_delete=models.SET_NULL, blank=True, null=True)
    encargos_resultados = models.ForeignKey(Proveedores, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.nombre


class Servicio_Optica(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    servicio = models.ForeignKey(Servicio, on_delete=models.SET_NULL, blank=True, null=True)
    optica = models.ForeignKey(OpticaSolyGafas, on_delete=models.SET_NULL, blank=True, null=True)


class Servicio_Persona(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    cliente = models.ForeignKey(Persona, on_delete=models.SET_NULL, blank=True, null=True, related_name='servicios_cliente')
    medico = models.ForeignKey(Persona, on_delete=models.SET_NULL, blank=True, null=True, related_name='servicios_medico')
    servicio = models.ForeignKey(Servicio, on_delete=models.SET_NULL, blank=True, null=True)


class Persona_Optica(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    persona = models.ForeignKey(Persona, on_delete=models.SET_NULL, blank=True, null=True)
    optica = models.ForeignKey(OpticaSolyGafas, on_delete=models.SET_NULL, blank=True, null=True)


class Compra(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    fecha = models.DateField(null=True)
    valor_total = models.FloatField(null=True)
    pago = models.BooleanField(default=False)
    persona = models.ForeignKey(Persona, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.id


class Producto(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=30, null=True)
    marca = models.CharField(max_length=30, null=True)
    valor = models.FloatField(null=True)
    descripcion = models.TextField(null=True)
    stock = models.IntegerField(null=True)
    optica = models.ForeignKey(OpticaSolyGafas, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.nombre


class Producto_Compra(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    cantidad = models.FloatField(null=True)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, blank=True, null=True)
    compra = models.ForeignKey(Compra, on_delete=models.SET_NULL, blank=True, null=True)