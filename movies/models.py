from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length = 80)
    
class Person(models.Model):
    name = models.CharField(max_length = 120)

class Job(models.Model):
    name = models.CharField(max_length = 128)
    
class Movie(models.Model):
   
    title = models.CharField(max_length = 200)
    overviw = models.TextField()
    release_date = models.DateField()
    running_time = models.IntegerField()
    budget = models.IntegerField(blank = True)
    tmndb_id = models.IntegerField(blank = True)
    revenue = models.IntegerField(blank = True)
    poster_path = models.URLField(blank = True)
    genres = models.ManyToManyField(Genre)
    credis = models.ManyToManyField(Person, through="MovieCredits")
    
class MovieCredits(models.Model):
    person = models.ForeignKey(Person,  on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,  on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)