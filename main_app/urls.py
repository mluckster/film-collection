from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('films/', views.films_index, name='films_index'),
]