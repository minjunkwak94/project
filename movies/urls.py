from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail_create_rank),
    path('<int:movie_pk>/ranks/', views.rank_list),
    path('<int:rank_pk>/', views.rank_detail_update_delete),    
]