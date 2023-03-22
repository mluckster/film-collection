from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Film

# Create your views here.
def home(request):
    return render(request, 'home.html')

def films_index(request):
    films = Film.objects.all()
    return render(request, 'films/index.html', { 'films' : films })

def film_detail(request, film_id):
    film = Film.objects.get(id=film_id)
    return render(request, 'films/detail.html', { 'film': film })

class FilmCreate(CreateView):
    model = Film
    fields = '__all__'

class FilmUpdate(UpdateView):
    model = Film
    fields = '__all__'

class FilmDelete(DeleteView):
    model = Film
    success_url = '/films/'
