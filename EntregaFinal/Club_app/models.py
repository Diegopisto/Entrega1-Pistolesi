from django.db import models

# Create your models here.

class Alumnos(models.Model):

    nombre=models.CharField(max_length=40)
    edad=models.IntegerField()
    actividad=models.CharField(max_length=40)
    turno=models.CharField(max_length=40)

    def __str__(self):
        return f"{self.nombre} - {self.edad} - {self.actividad} - {self.turno}"
    class Meta():
        ordering = ("nombre", "edad", "actividad", "turno")

class Profesores(models.Model):

    nombre=models.CharField(max_length=40)
    actividad=models.CharField(max_length=40)
    turno=models.CharField(max_length=40)

    def __str__(self):
        return f"{self.nombre} - {self.actividad} - {self.turno}"

    class Meta():
        ordering = ("nombre", "actividad", "turno")

class Actividades(models.Model):

    actividad=models.CharField(max_length=40)
    turno=models.CharField(max_length=40)

    def __str__(self):
        return f"{self.actividad} - {self.turno}"

    class Meta():
        ordering = ("actividad", "turno")
    
