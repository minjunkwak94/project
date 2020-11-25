from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    path('<int:movie_pk>/ranks/', views.rank_create, name='rank_create'),
    path('<int:movie_pk>/ranks/<int:rank_pk>/delete/', views.rank_delete, name='rank_delete'), 
    path('<int:movie_pk>/ranks/<int:rank_pk>/update/', views.rank_update, name='rank_update'), 
    path('recommended/', views.movies_recommended, name='movies_recommended'), 
    # path('', views.movie_list),
    # path('<int:movie_pk>/', views.movie_detail),
    # path('<int:movie_pk>/ranks/', views.rank_list_create),
    # path('<int:movie_pk>/ranks/<int:rank_pk>/', views.rank_update_delete),
]