from django.db import models

class Departamento(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre
