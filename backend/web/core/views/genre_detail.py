from django.http import HttpRequest,HttpResponse
from django.shortcuts import render
from django.views.generic import View,DetailView,ListView
from ..models import Genre,Author
from django.db.models import Prefetch

from ..models.author import TypeChoices


class GenreDetailView(ListView):
    template_name = "core/genre_detail.html"
    model = Author
    def get_queryset(self):
        genre = Genre.objects.get(slug=self.kwargs.get('slug'))
        #genre = Genre.objects.prefetch_related(
            #Prefetch("authors", queryset=Author.objects.filter(century__slug=self.century))
        #).filter(authors__century__slug=self.century).distinct()
        if genre.type == TypeChoices.DIRECTOR:
            return genre.films.all()
        if genre.parent:
            return genre.authors.all()
        else:
            return genre.children.all()

