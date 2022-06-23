from django.db import models
from datetime import *

# Create your models here.

# class Persona(models.Model):
    
#     nombre = models.CharField("Nombre",max_length=40)
#     apellido = models.CharField("Apellido",max_length=40)
#     RELACIONES = (
#         (1, "Papá/Mamá"),
#         (2, "Hermano/Hermana"),
#         (3, "Tío/Tía"),
#         (4, "Abuelo/Abuela"),
#         (5, "Primo/Prima")
#     )
#     relacion = models.PositiveSmallIntegerField("Relación",choices=RELACIONES)
#     anio_nacimiento = models.DateTimeField("Fecha Nacimiento")

class Familiare(models.Model):
    
    nombre = models.CharField("Nombre",max_length=40)
    apellido = models.CharField("Apellido",max_length=40)
    RELACIONES = (
        (1, "Papá"),
        (2, "Mamá"),
        (3, "Hermano"),
        (4, "Hermana"),
        (5, "Tío"),
        (6, "Tía"),
        (7, "Abuelo"),
        (8, "Abuela"),
        (9, "Primo"),
        (10, "Prima"),
    )
    relacion = models.PositiveSmallIntegerField("Relación",choices=RELACIONES)
    edad = models.IntegerField("Edad")
    fecha = models.DateField("Fecha Nacimiento")