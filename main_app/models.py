from django.db import models
from django.urls import reverse

# Create your models here.
class Film(models.Model):
    title = models.CharField(max_length = 200)
    release_year = models.IntegerField()
    director = models.CharField(max_length = 100)

    def get_absolute_url(self):
        return reverse('film_detail', kwargs= { 'film_id': self.id })