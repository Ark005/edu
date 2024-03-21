from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import View
from ..models import Author
from django.views.generic import DetailView


class AuthorDetail(DetailView):
    context_object_name = 'author'
    model = Author
    template_name = 'core/author_detail.html'


def get_author_object(slug: str):
    try:
        author_object = Author.objects.get(slug=slug)
    except:
        return False

    return author_object

def author_detail_view(request: HttpRequest, slug: str):
    author_object = get_author_object(slug)
    if author_object == False:
        return HttpResponse(status=404)
    return render(request, template_name='core/author_details.html', context={'author': author_object})

# Синтаксис шаблона:
# {% if condition (например song.analysis != None или просто song.analysis) %}
#
# <div>THIS WILL BE RENDERED IF CONDITION PASSES</div>
#
# {% else %}
# 
# <div>THIS WILL BE RENDERED IF CONDITION NOT PASSES</div>
# {% endif %}
#
#
