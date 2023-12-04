from ..models import Author
from django.shortcuts import render

def get_author_list():
    objectlist = Author.objects.all().order_by('year')
    return objectlist

def author_list_view(request):
    context = get_author_list()
    return render(request,template_name='core/author_list.html', context={'author_list':context})
