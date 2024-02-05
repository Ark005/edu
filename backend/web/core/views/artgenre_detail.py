from django.http import HttpRequest,HttpResponse
from django.shortcuts import render
from django.views.generic import View,DetailView
from ..models import Genre,Artgenre


class ArtGenreDetailView(DetailView):
    template_name = "core/art_detail.html"
    model = Artgenre
    
   