from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list),
<<<<<<< HEAD
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/ranks/', views.rank_list_create),
    path('<int:movie_pk>/ranks/<int:rank_pk>/', views.rank_update_delete),    
=======
    path('<int:movie_pk>/', views.movie_detail_create_rank),
    path('<int:movie_pk>/ranks/', views.rank_list),
    path('<int:rank_pk>/', views.rank_detail_update_delete),    
>>>>>>> minjun
]