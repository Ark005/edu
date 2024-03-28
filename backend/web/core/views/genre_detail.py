from django.http import HttpRequest,HttpResponse
from django.shortcuts import render
from django.views.generic import View,DetailView,ListView
from ..models import Genre,Author


class GenreDetailView(ListView):
    template_name = "core/genre_detail.html"
    model = Author
    def get_queryset(self):
        genre = Genre.objects.get(slug=self.kwargs.get('slug'))
        if genre.parent:
            return genre.authors.all()
        else:
            return genre.children.all()
    
