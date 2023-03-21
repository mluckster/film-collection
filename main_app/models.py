from django.db import models

# Create your models here.
class Film(models.Model):
    title = models.CharField(max_length = 200)
    release_year = models.IntegerField()
    director = models.CharField(max_length = 100)