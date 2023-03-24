from django.db import models
from django.urls import reverse

# Create your models here.

RATINGS = [
    ('5', '5 Stars'),
    ('4.5', '4.5 Stars'),
    ('4', '4 Stars'),
    ('3.5', '3.5 Stars'),
    ('3', '3 Stars'),
    ('2.5', '2.5 Stars'),
    ('2', '2 Stars'),
    ('1.5', '1.5 Stars'),
    ('1', '1 Star'),
    ('0.5', 'Half a Star'),
    ('0', 'Zero Stars')
]

class Actor(models.Model):
    name = models.CharField(max_length=75)
    dob = models.DateField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('film_detail', kwargs= { 'film_id': self.id })

class Film(models.Model):
    title = models.CharField(max_length = 200)
    release_year = models.IntegerField()
    director = models.CharField(max_length = 100)
    actors = models.ManyToManyField(Actor)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('film_detail', kwargs= { 'film_id': self.id })
    
class Reviews(models.Model):
    body = models.CharField(max_length=1000)
    rating = models.CharField(
        max_length=5,
        choices=RATINGS,
        default=RATINGS[5][0]
    )
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.get_rating_display()} for {self.film} review: {self.body}"
    