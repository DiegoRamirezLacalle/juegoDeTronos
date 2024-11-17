from django.db import models

class Departamento(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()

    def __str__(self):
<<<<<<< HEAD
        return self.name

class Season(models.Model):
    number = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return f"Season {self.number}"

class Character(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    house = models.ForeignKey(House, related_name='characters', on_delete=models.CASCADE)
    seasons = models.ManyToManyField(Season, related_name='characters')
    image = models.ImageField(upload_to='characters/') 

    def __str__(self):
        return self.name
=======
        return self.nombre
>>>>>>> parent of 9e34442 (funcionalidad de la pagina web)
