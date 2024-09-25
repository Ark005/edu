from django.db.models import Min, Max
from django.shortcuts import render
from ..models import Category, Author, Genre, Film, Century, SuperCategory
from ..models.author import get_century_choices
from django.http import HttpResponse, HttpRequest
import random


def get_all_authors():
    author_list = Author.objects.all()
    return author_list


def get_author_centuries():
    centuries = Century.objects.all().order_by('value')
    return centuries


def get_random_ids(limit: int = 4) -> list[int]:
    authors_dict = Author.objects.all().aggregate(min=Min("id"), max=Max("id"))
    min_id = authors_dict["min"]
    max_id = authors_dict["max"]
    random_numbers = [random.randint(min_id, max_id) for _ in range(limit)]
    return random_numbers


def get_author_by_id(_id: int) -> Author:
    author = Author.objects.filter(id=_id).first()
    if not author:
        return get_author_by_id(_id + 1)
    return author


def get_random_cards() -> list[Author]:
    random_ids = get_random_ids()
    random_authors = []
    for i in random_ids:
        author = get_author_by_id(i)
        random_authors.append(author)
    return random_authors


def index_view(request):
    supercategory_list = SuperCategory.objects.all().order_by("name")
    centuries = get_author_centuries()
    genre_list = Genre.objects.all()
    film_list = Film.objects.all()
    random_cards = get_random_cards()

    return render(
        request,
        'index.html',
        {
            'object_list': supercategory_list,
            'centuries': centuries,
            'genre_list': genre_list,
            'film_list': film_list,
            'random_cards': random_cards
        }
    )

