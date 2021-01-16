from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Tipo(models.Model):
    nombre = models.CharField(max_length=200, verbose_name= "nombre")

    class Meta:
        verbose_name = "Tipo"
        verbose_name_plural = "Tipos"
        ordering = ['id', 'nombre']

    def __str__(self):
        return self.nombre 

class Estado(models.Model):
    nombre = models.CharField(max_length=200, verbose_name= "nombre")

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"
        ordering = ['id', 'nombre']

    def __str__(self):
        return self.nombre 

class Prioridad(models.Model):
    nombre = models.CharField(max_length=200, verbose_name= "nombre")

    class Meta:
        verbose_name = "Prioridad"
        verbose_name_plural = "Prioridades"
        ordering = ['id', 'nombre']

    def __str__(self):
        return self.nombre 

class Criticidad(models.Model):
    nombre = models.CharField(max_length=200, verbose_name= "nombre")

    class Meta:
        verbose_name = "Criticidad"
        verbose_name_plural = "Criticidades"
        ordering = ['id', 'nombre']

    def __str__(self):
        return self.nombre 



class Solicitud(models.Model):
    nombre = models.CharField(max_length=200, verbose_name= "título")
    descripcion = models.TextField(verbose_name= "Descripción", default="")
    usuario_solicitante = models.ForeignKey(User, on_delete=models.CASCADE, null=True,  default=1)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, null=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=False, blank=False, default= 1)
    fecha_ingreso = models.DateTimeField(auto_now_add=True, null=True)
    prioridad = models.ForeignKey(Prioridad, on_delete=models.CASCADE, null=True, default= 1)
    criticidad = models.ForeignKey(Criticidad, on_delete=models.CASCADE, null=True, default= 1)
    archivo = models.FileField(upload_to="productos", null=True, blank=True)
    


    class Meta:
        verbose_name = "Solicitud"
        verbose_name_plural = "Solicitudes"
        ordering = ['id', 'nombre']

    def __str__(self):
        return self.nombre 

class Imputacion(models.Model):
    observacion = models.CharField(max_length=200, verbose_name= "Observación")
    hh = models.FloatField(null=True, blank=True, verbose_name= "HH")
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Imputación"
        verbose_name_plural = "Imputaciones"
        ordering = ['id', 'observacion']

    def __str__(self):
        return self.observacion 