from django.shortcuts import render
from .models import Film

# Create your views here.
def home(request):
    return render(request, 'home.html')

def films_index(request):
    films = Film.objects.all()
    return render(request, 'films/index.html', { 'films' : films })