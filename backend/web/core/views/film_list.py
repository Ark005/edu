from ..models import Film
from django.shortcuts import render

def get_film_list():
    objectlist = Film.objects.all()
    return objectlist

def film_list_view(request):
    context = get_film_list()
    return render(request,template_name='core/film_list.html', context={'film_list':context})

