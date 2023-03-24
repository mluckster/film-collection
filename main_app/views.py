from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Film, Reviews, Actor
from .forms import ReviewsForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def films_index(request):
    films = Film.objects.all()
    return render(request, 'films/index.html', { 'films' : films })

def film_detail(request, film_id):
    film = Film.objects.get(id=film_id)
    actors_not_in_film = Actor.objects.exclude(id__in = film.actors.all().values_list('id'))
    review_form = ReviewsForm()
    return render(request, 'films/detail.html', { 
        'film': film ,
        'review_form': review_form,
        'actors': actors_not_in_film
    })

class FilmCreate(CreateView):
    model = Film
    fields = '__all__'

class FilmUpdate(UpdateView):
    model = Film
    fields = '__all__'

class FilmDelete(DeleteView):
    model = Film
    success_url = '/films/'

def add_review(request, film_id):
    form = ReviewsForm(request.POST)
    if form.is_valid():
        new_review=form.save(commit=False)
        new_review.film_id=film_id
        new_review.save()
    return redirect('film_detail', film_id=film_id)

class ActorCreate(CreateView):
    model = Actor
    fields = '__all__'

def assoc_actor(request, film_id):
    Film.objects.get(id=film_id).actors.add(request.POST['actor'])
    return redirect('film_detail', film_id=film_id)
