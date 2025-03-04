from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Costa(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cabaña = models.IntegerField()
    fechaEstadia = models.DateField()
    def __str__(self):
        return f"{self.nombre}"

class Natur(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cabaña = models.IntegerField()
    fechaEstadia = models.DateField()
    def __str__(self):
        return f"{self.nombre}"

class Rayen(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cabaña = models.IntegerField()
    fechaEstadia = models.DateField()
    def __str__(self):
        return f"{self.nombre}"
    
class Vulcanche(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cabaña = models.IntegerField()
    fechaEstadia = models.DateField()
    def __str__(self):
        return f"{self.nombre}"
    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"