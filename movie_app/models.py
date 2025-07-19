from django.db import models

class Movie_data(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    director = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
