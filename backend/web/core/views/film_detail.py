from django.http import HttpRequest,HttpResponse
from django.shortcuts import render
from django.views.generic import View
from ..models import Film

# TODO: Создать новое представление основанное на классах
# с аналогичным функционалом. Наследуйтесь от DetailView.
# Реализуйте функционал аналогичный функции author_detail_view

from django.views.generic import DetailView

class FilmDetailView(DetailView):
    context_object_name = 'film'
    model = Film
    template_name = 'core/film_detail.html'
    
