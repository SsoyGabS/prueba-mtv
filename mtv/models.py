from unittest.util import _MAX_LENGTH
from django.db import models

class familia(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=100)
    parentezco = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField(null=True)
    