from ..models import Genre, Filmgenre
from django.shortcuts import render

def get_film_list():
    objectlist = Filmgenre.objects.all()
    return objectlist

def film_list_view(request):
    context = get_film_list()
    return render(request,template_name='core/film_list.html', context={'film_list':context})


