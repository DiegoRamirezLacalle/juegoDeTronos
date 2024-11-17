from django.db import models

class House(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()


class Season(models.Model):
    number = models.PositiveIntegerField()
    description = models.TextField()


class Character(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    house = models.ForeignKey(House, related_name='characters', on_delete=models.CASCADE)
    seasons = models.ManyToManyField(Season, related_name='characters')
    image = models.ImageField(upload_to='characters/') 

    
