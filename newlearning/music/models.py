from django.db import models


class Album(models.Model):
    artist = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    album_title = models.CharField(max_length=200)
    album_logo = models.CharField(max_length=1200)

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=200)
    song_type = models.CharField(max_length=10)

