from ..models import Genre
from django.shortcuts import render

def get_genre_list():
    objectlist = Genre.objects.all()
    return objectlist

def genre_list_view(request):
    context = get_genre_list()
    return render(request,template_name='core/genre_list.html', context={'genre_detail':context})


