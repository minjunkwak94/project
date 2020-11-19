from django.db import models

# Create your models here.

class Movie(models.Model):    
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    video = models.BooleanField()
    poster_path = models.CharField(max_length=100)
    tmdb_id = models.IntegerField()
    adult = models.BooleanField()
    original_language = models.CharField(max_length=100)
    original_title = models.CharField(max_length=100)
    genre_ids = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    vote_average = models.FloatField()
    overview = models.TextField()
    release_date = models.CharField(max_length=100)

class Rank(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    star = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)