from ..models import Genre, Artgenre
from django.shortcuts import render

def get_art_list():
    objectlist = Artgenre.objects.all()
    return objectlist

def art_list_view(request):
    context = get_art_list()
    return render(request,template_name='core/art_list.html', context={'art_list':context})


