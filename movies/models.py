from django.db import models
from django.conf import settings
# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):    
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    video = models.BooleanField()
    poster_path = models.CharField(max_length=100)
    backdrop_path = models.CharField(max_length=100, null=True)
    tmdb_id = models.IntegerField()
    adult = models.BooleanField()
    original_language = models.CharField(max_length=100)
    original_title = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre)
    title = models.CharField(max_length=100)
    vote_average = models.FloatField()
    overview = models.TextField()
    release_date = models.CharField(max_length=100)

class Rank(models.Model):
    A = 5
    B = 4
    C = 3
    D = 2
    E = 1
    F = 0
    STARS = (
        (F, '☆☆☆☆☆ 나한테 돈을 주면 이것보다 잘 만들 자신이 있다고 느껴질 때'),
        (E, '★☆☆☆☆ 그래도 영화의 결말은 확인해야한다는 의무감으로 봤을 때 '),
        (D, '★★☆☆☆ 감동도 재미도 없지만 시간은 아깝지 않았다고 느껴질 때'),
        (C, '★★★☆☆ 심심할 때 보면 딱 좋은 영화에게는 별점 3개를'),
        (B, '★★★★☆ 극장에서 반드시 봐야할 영화, 나의 시간과 돈이 아깝지 않은 영화'),
        (A, '★★★★★ 이 영화가 개봉된 후 내가 태어났고 또한 살아있어서 감사함을 느낀다 '),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_rank')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_rank')
    star = models.PositiveIntegerField(default=0, choices=STARS)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)