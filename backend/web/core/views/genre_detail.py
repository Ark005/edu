from django.http import HttpRequest,HttpResponse
from django.shortcuts import render
from django.views.generic import View,DetailView
from ..models import Genre


class GenreDetailView(DetailView):
    template_name = "core/genre_detail.html"
    model = Genre
    
   