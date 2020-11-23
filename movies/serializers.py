from rest_framework import serializers
from .models import Movie, Rank, Genre

class RankSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rank
        fields = ('user', 'movie', 'star')
        read_only_fields = ('user', 'movie')


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields =('title', 'poster_path', 'backdrop_path', 'vote_average', 'genres', 'overview')

<<<<<<< HEAD

=======
>>>>>>> minjun
class MovieDetailSerializer(serializers.ModelSerializer):

    rank_set = RankSerializer(
        many=True,
        read_only=True,
<<<<<<< HEAD
    )

    class Meta:
        model = Movie
        fields = ('popularity','vote_count', 'video', 'poster_path', 'backdrop_path', 'tmdb_id', 'adult', 'original_language', 'original_title', 'genres', 'title', 'vote_average', 'overview', 'release_date', 'rank_set')
=======
    ) 


    class Meta:
        model = Movie
        fields = ('popularity','vote_count', 'video', 'poster_path', 'backdrop_path', 'tmdb_id', 'adult', 'original_language', 'original_title', 'genres', 'title', 'vote_average', 'overview', 'release_date', 'rank_set')

>>>>>>> minjun
