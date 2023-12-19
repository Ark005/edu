from ..models import Genre
from django.shortcuts import render

from ..models.fil_genre import FilGenre


def get_fil_genre_list():
    objectlist = FilGenre.objects.all()
    return objectlist

def genre_list_view(request):
    context = get_fil_genre_list()
    return render(request,template_name='core/fil_genre_list.html', context={'fil_genre_list':context})


