from django.shortcuts import render
from ..models import Category, Author, Genre, Film, Century, SuperCategory
from ..models.author import get_century_choices
from django.http import HttpResponse, HttpRequest


def get_all_authors():
    author_list = Author.objects.all()
    return author_list


def get_author_centuries():
    centuries = Century.objects.all().order_by('value')
    return centuries


def index_view(request):
    supercategory_list = SuperCategory.objects.all().order_by("name")
    centuries = get_author_centuries()
    genre_list = Genre.objects.all()
    film_list = Film.objects.all()

    return render(
        request,
        'index.html',
        {
            'object_list': supercategory_list, 'centuries': centuries, 'genre_list': genre_list, 'film_list': film_list}
    )

