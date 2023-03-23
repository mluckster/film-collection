from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Film, Reviews
from .forms import ReviewsForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def films_index(request):
    films = Film.objects.all()
    return render(request, 'films/index.html', { 'films' : films })

def film_detail(request, film_id):
    film = Film.objects.get(id=film_id)
    review_form = ReviewsForm()
    return render(request, 'films/detail.html', { 
        'film': film ,
        'review_form': review_form,
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
