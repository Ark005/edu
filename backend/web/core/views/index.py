from django.shortcuts import render
from ..models import Category,Author,Genre,Film
from ..models.author import get_century_choices
from django.http import HttpResponse,HttpRequest


def get_all_authors():

    author_list = Author.objects.all()
    return author_list

def get_author_centuries():
    
    author_centuries_list = []
    for author in get_all_authors():
        author_centuries_list.append(author.century)

    all_centuries = get_century_choices()
    filtered_centuries = []
    for century in all_centuries:
        if century[0] in author_centuries_list:
            filtered_centuries.append(century)
    return filtered_centuries

def index_view(request):
   

    category_list  = Category.objects.all()
    centuries = get_author_centuries()
    genre_list = Genre.objects.all()
    film_list = Film.objects.all()
    
    return render(request, 'index.html', {
        'categories': category_list, 'centuries': centuries, 'genre_list': genre_list, 'film_list': film_list}
        )

def index_detail_view(request: HttpRequest, slug: str):
   
    category_object = get_category_object(slug)
    if category_object == False: 
        return HttpResponse(status=404)
    return render(request, template_name='core/index.html', context={'category': category_object})

