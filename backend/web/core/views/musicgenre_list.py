from ..models import Musicgenre
from django.shortcuts import render

def get_music_list():
    objectlist = Musicgenre.objects.all()
    return objectlist

def music_list_view(request):
    context = get_music_list()
    return render(request,template_name='core/music_list.html', context={'music_list':context})


