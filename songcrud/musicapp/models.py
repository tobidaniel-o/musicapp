from email.policy import default
from turtle import title
from django.db import models
from datetime import datetime

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()

class Song(models.Model):
    Artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    date_released = models.DateField(default=datetime.today)
    likes = models.CharField(max_length=10)
    artiste_id = models.IntegerField()
class Lyric(models.Model):
    Song = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.CharField(max_length=400)
    song_id = models.IntegerField()

# An Artiste can have multiple songs - one to many relationships - foreign key attribute is specified
 
# a song can have multiple lyrics. - one to many relationships - foreign key attribute is specified
 
# A song must only belong to one Artiste - one to one relationship
 
# a lyric must only belong to a song - one to one relationship
 
# You are to specify the foreignkey relationship yourself.
 
# Also, the model field attributes should be specified by you. 
