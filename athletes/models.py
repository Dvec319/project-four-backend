from django.db import models

# Create your models here.

class Athlete(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    sport = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    year = models.IntegerField()
    image = models.CharField(max_length=200)
