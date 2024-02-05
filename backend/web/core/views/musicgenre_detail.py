from django.http import HttpRequest,HttpResponse
from django.shortcuts import render
from django.views.generic import View,DetailView
from ..models import Genre,Musicgenre


class MusicGenreDetailView(DetailView):
    template_name = "core/musicgenre_detail.html"
    model = Musicgenre
    
   