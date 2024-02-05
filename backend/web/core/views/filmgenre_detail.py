from django.http import HttpRequest,HttpResponse
from django.shortcuts import render
from django.views.generic import View,DetailView
from ..models import Genre,Filmgenre


class FilmGenreDetailView(DetailView):
    template_name = "core/film_detail.html"
    model = Filmgenre
    
   