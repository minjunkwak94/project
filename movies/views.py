from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status
from django.core.paginator import Paginator

from .models import Genre, Movie, Rank
from .forms import RankForm
# from .serializers import RankSerializer, MovieDetailSerializer, MovieListSerializer


@require_GET
def movie_list(request):
    movies = Movie.objects.order_by('pk')
    paginator = Paginator(movies, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'movies': movies,
        'page_obj' : page_obj,
    }
    return render(request, 'movies/movie_list.html', context)


@require_GET
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    rank_form = RankForm()
    ranks = movie.movie_rank.all()
    # ranks = Rank.objects.filter(movie=movie)
    total = 0
    num = len(ranks)
    for r in ranks:
        total += r.star
    if total != 0:
        avg = round(total / num, 1)
    else:
        avg = 0
    context = {
        'movie': movie,
        'rank_form': rank_form,
        'ranks': ranks,
        'avg' : avg,
    }
    return render(request, 'movies/movie_detail.html', context)

@login_required
def rank_update(request, movie_pk, rank_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    rank = get_object_or_404(Rank, pk=rank_pk)
    rank_form = RankForm()
    ranks = movie.movie_rank.all()      
    total = 0
    num = len(ranks)
    for r in ranks:
        total += r.star
    if total != 0:
        avg = round(total / num, 1)
    else:
        avg = 0
    if request.user == rank.user:
        if request.method == 'POST':
            form = RankForm(request.POST, instance=rank)
            if form.is_valid():
                rank = form.save(commit=False)
                rank.user = request.user
                rank.movie = movie
                rank.save()
                return redirect('movies:detail', movie.pk)
        else:
            form = RankForm(instance=rank)        
        context = {
            'movie': movie,
            'rank_form': form,
            'ranks': ranks,
            'avg' : avg,
        }
        return render(request, 'movies/movie_detail.html', context)    
    else:
        return redirect('movies:detail', movie.pk)
 

 
@require_POST
@login_required
def rank_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    rank_form = RankForm(request.POST)
    if rank_form.is_valid():
        rank = rank_form.save(commit=False)
        rank.movie = movie
        rank.user = request.user
        rank.save()
        return redirect('movies:movie_detail', movie.pk)
    context = {
        'movie': movie,
        'rank_form': rank_form,
        'ranks': movie.rank_set.all(),
    }
    return render(request, 'community/detail.html', context)
  

@require_POST
@login_required
def rank_delete(request, movie_pk, rank_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    rank = get_object_or_404(Rank, movie=movie, pk=rank_pk)
    rank.delete()
    return redirect("movies:movie_list")

@login_required
@require_GET
def movies_recommended(request):    
    ranks = request.user.user_rank.all()
    selected_ranks = []        

    #일정 평점 이상만 골라낸다
    for rank in ranks:
        if rank.star >= 4:
            selected_ranks.append(rank)
    
    target_genres = []        
    # 일정 평점 이상의 장르들 골라낸다
    for rank in selected_ranks:
        genres = rank.movie.genres.all()
        for genre in genres:
            target_genres.append(genre)
    target_genres = list(set(target_genres))
    # print(target_genres)
    movies = Movie.objects.all()
    target_movies = []
    for target_genre in target_genres:
        for movie in movies:        
            if target_genre in movie.genres.all():
                target_movies.append(movie)
                continue
    # print(target_movies)
    paginator = Paginator(target_movies, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'movies': movies,
        'page_obj' : page_obj,
    }
    return render(request, 'movies/movies_recommended.html', context)



    # print(request.user.rank_set)
    return redirect("movies:movie_list")
        

# @api_view(['GET'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieListSerializer(movies, many=True)
#         return Response(serializer.data)


# @api_view(['GET'])
# def movie_detail(request, movie_pk):
#     movie = get_object_or_404(Movie, pk=movie_pk)
#     serializer = MovieDetailSerializer(movie)            
#     return Response(serializer.data)

        
# @api_view(['GET', 'POST'])
# def rank_list_create(request, movie_pk):
#     movie = get_object_or_404(Movie, pk=movie_pk)
#     if request.method == 'GET':
#         ranks = movie.rank_set.all()
#         serializer = RankSerializer(ranks, many=True)
#         return Response(serializer.data)
#     else:
#         serializer = RankSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save(movie=movie, user=request.user)
#             return Response(serializer.data)


# @api_view(['PUT', 'DELETE'])
# def rank_update_delete(request, movie_pk, rank_pk):
#     movie = get_object_or_404(Movie, pk=movie_pk)
#     rank = get_object_or_404(Rank, movie=movie, pk=rank_pk)
#     if request.method == 'PUT':
#         serializer = RankSerializer(rank, data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
#     else:
#         rank.delete()
#         return Response({ 'success delete rank!': rank_pk })
