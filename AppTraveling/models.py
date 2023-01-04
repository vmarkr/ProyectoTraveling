from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class viajero(models.Model):
    def __str__(self):
        return f"Viajero:{self.nombre} {self.apellido}---{self.destino}"
    
    nombre   = models.CharField(max_length=50)
    apellido = models.CharField(max_length=40)
    correo   = models.EmailField()
    destino  = models.CharField(max_length=50) 
    edad     = models.IntegerField()
    adulto   = models.BooleanField(default=False)
    
class destino (models.Model):
    def __str__(self):
        return f"Destino:{self.nombre}"
    
    nombre     = models.CharField(max_length=50)
    comentario = models.TextField()

class alojamiento (models.Model):
    def __str__(self):
        return f"Alojamiento:{self.nombre} - {self.ubicacion}"
    
    nombre                = models.CharField(max_length=100)
    ubicacion             = models.CharField(max_length=100)
    cantidad_habitaciones = models.IntegerField()
    cantidad_personas     = models.IntegerField()
    mascotas              = models.BooleanField(default=False)

class vuelos (models.Model):
    def __str__(self):
        return f"Vuelo:{self.numero} - {self.destino}"
    
    numero                = models.IntegerField()
    destino               = models.CharField(max_length=100)
    origen                = models.CharField(max_length=100)
    salida                = models.DateField()
    llegada               = models.DateField()
    cantidad_pasajes      = models.IntegerField()
    empresa               = models.CharField(max_length=100)