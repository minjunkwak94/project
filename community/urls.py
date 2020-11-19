from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list_create),
    path('<int:post_pk>/', views.post_detail_update_delete),
    path('<int:post_pk>/comment/', views.comment_list_create),
    path('<int:post_pk>/comment/<int:comment_pk>/', views.comment_delete),
]