from django.http import HttpRequest,HttpResponse
from django.shortcuts import render
from django.views.generic import View
from ..models import Author, Video
from django.views.generic import DetailView

class VideoDetail(DetailView):
    context_object_name = 'video'
    model = Video
    #template_name = 'core/author_detail.html'

def get_video_object(slug: str):

    try:
        video_object = Video.objects.get(slug=slug)
    except:
        return False

    return video_object

# if [условие (==, !=, <, >, is, <= ... )] :
#    ... Код который выполнится в случае выполнения условия
# else (не обязательно):
#    ... код который выполнится, в случае если условие не выполнится


def video_detail_view(request: HttpRequest, slug: str):
   
    video_object = get_video_object(slug)
    if video_object == False:
        return HttpResponse(status=404)
    return render(request, template_name='core/author_details.html', context={'video': video_object})

#Синтаксис шаблона:
#{% if condition (например song.analysis != None или просто song.analysis) %} 
#
# <div>THIS WILL BE RENDERED IF CONDITION PASSES</div>
#
#{% else %}
# 
# <div>THIS WILL BE RENDERED IF CONDITION NOT PASSES</div>
#{% endif %}
#
#
