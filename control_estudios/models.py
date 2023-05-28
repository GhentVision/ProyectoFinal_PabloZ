from django.db import models
from django.contrib.auth.models import User

class Curso(models.Model):
    elegir_duracion = [
        ('1 mes', '1 mes'),
        ('2 meses', '2 meses'),
        ('3 meses', '3 meses'),
        ('4 meses', '4 meses')
        ]
    nombre = models.CharField(max_length=60)
    comision = models.IntegerField()
    descripcion = models.CharField(max_length=800, default='Descripción pendiente')
    duracion = models.CharField(max_length=60, choices=elegir_duracion, default='1 mes')
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.nombre} | {self.comision}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    fecha_nac = models.DateField()
    dni = models.CharField(max_length=32)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    fecha_nac = models.DateField()
    dni = models.CharField(max_length=32)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    profesion = models.CharField(max_length=128)
    bio = models.TextField()
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"