from django.shortcuts import render, get_object_or_404, get_list_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Genre, Movie, Rank
from .serializers import RankSerializer, MovieDetailSerializer, MovieListSerializer


@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieDetailSerializer(movie)            
    return Response(serializer.data)

        
@api_view(['GET', 'POST'])
def rank_list_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        ranks = movie.rank_set.all()
        serializer = RankSerializer(ranks, many=True)
        return Response(serializer.data)
    else:
        serializer = RankSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=request.user)
            return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
def rank_update_delete(request, movie_pk, rank_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    rank = get_object_or_404(Rank, movie=movie, pk=rank_pk)
    if request.method == 'PUT':
        serializer = RankSerializer(rank, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        rank.delete()
        return Response({ 'success delete rank!': rank_pk })