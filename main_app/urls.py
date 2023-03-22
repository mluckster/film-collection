from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('films/', views.films_index, name='films_index'),
    path('films/<int:film_id>/', views.film_detail, name='film_detail'),
    path('films/create/', views.FilmCreate.as_view(), name="films_create"),
    path('films/<int:pk>/delete/', views.FilmDelete.as_view(), name='film_delete'),
    path('film/<int:pk>/update/', views.FilmUpdate.as_view(), name='film_update')
]