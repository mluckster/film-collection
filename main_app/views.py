from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Film, Reviews, Actor
from .forms import ReviewsForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required
def films_index(request):
    films = Film.objects.filter(users = request.user)
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

class FilmCreate(LoginRequiredMixin, CreateView):
    model = Film
    fields = ['title', 'release_year', 'director']

    def form_valid(self, form):
        form.instance.users = self.request.user
        return super().form_valid(form)

class FilmUpdate(LoginRequiredMixin, UpdateView):
    model = Film
    fields = ['title', 'release_year', 'director']

class FilmDelete(LoginRequiredMixin, DeleteView):
    model = Film
    success_url = '/films/'

@login_required
def add_review(request, film_id):
    form = ReviewsForm(request.POST)
    if form.is_valid():
        new_review=form.save(commit=False)
        new_review.film_id=film_id
        new_review.save()
    return redirect('film_detail', film_id=film_id)

class ActorCreate(LoginRequiredMixin, CreateView):
    model = Actor
    fields = '__all__'
    success_url = '/films/'

@login_required
def assoc_actor(request, film_id):
    Film.objects.get(id=film_id).actors.add(request.POST['actor'])
    return redirect('film_detail', film_id=film_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = { 'form': form, 'error_message': error_message }
    return render(request, 'registration/signup.html', context)
