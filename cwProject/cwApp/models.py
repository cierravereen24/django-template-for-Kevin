from django.db import models


# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=150, default="")
    yearReleased = models.DateField()
    ageAllowed = models.IntegerField()
    genre = models.CharField(max_length=150, default="")
