from django.contrib import admin
from .models import Film, Reviews, Actor

# Register your models here.
admin.site.register(Film)
admin.site.register(Reviews)
admin.site.register(Actor)