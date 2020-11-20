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


@api_view(['POST','GET'])
def movie_detail_create_rank(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        serializer = RankSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=user)
            return Response(serializer.data)
    elif request.method == 'GET':
        serializer = MovieDetailSerializer(movie)            
        return Response(serializer.data)

@api_view(['GET'])        
def rank_list(request, movie_pk):
    ranks = get_list_or_404(Rank)
    serializer = RankSerializer(ranks, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def rank_detail_update_delete(request, rank_pk):
    rank = get_object_or_404(Rank, pk=rank_pk)
    if request.method == 'GET':
        serializer = RankSerializer(rank)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = RankSerializer(rank, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        comment.delete()
        return Response({ 'id': rank_pk })
