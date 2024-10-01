from typing import Any

from django.db.models import Min, Max, Model
from django.shortcuts import render
from ..models import Category, Author, Genre, Film, Century, SuperCategory
from ..models.author import get_century_choices, author_type_choices, TypeChoices
from django.http import HttpResponse, HttpRequest
import random


def get_all_authors():
    author_list = Author.objects.all()
    return author_list


def get_author_centuries():
    centuries = Century.objects.all().order_by('value')
    return centuries


def get_random_model_ids(model, filter_data: dict, limit: int = 4) -> list[int]:
    model_dict = model.objects.filter(**filter_data).values("id")
    random_numbers = [random.choice(model_dict)["id"] for _ in range(limit)]
    return list(set(random_numbers))


def get_entity_by_id(model_class, _id: int) -> Author:
    obj = model_class.objects.filter(id=_id).first()
    if not obj or not obj.image:
        return get_entity_by_id(model_class, _id + 1)
    return obj


def get_random_cards(model_class, filter_data: dict, limit: int = 4) -> list[Any]:
    random_ids = get_random_model_ids(model_class, filter_data, limit)
    random_cards = []
    for i in random_ids:
        obj = get_entity_by_id(model_class, i)
        random_cards.append(obj)
    return random_cards


def get_random_authors_by_types():
    authors_by_types = {}
    exclude_author_types = [TypeChoices.LECTOR, TypeChoices.DIRECTOR]
    for _type, _ in author_type_choices:
        if _type not in exclude_author_types:
            authors_by_types[_type] = get_random_cards(Author, {"type": _type})
    return authors_by_types


def get_random_films() -> list[Film]:
    return get_random_cards(Film, {})


def index_view(request):
    supercategory_list = SuperCategory.objects.all().order_by("name")
    centuries = get_author_centuries()
    genre_list = Genre.objects.all()
    random_cards = get_random_cards(Author, {})
    children_items = get_random_cards(Author, {"genre__name": "Детская литература"})
    silver_items = get_random_cards(Author, {"genre__name": "Поэты Серебрянного века"})

    return render(
        request,
        'index.html',
        {
            'object_list': supercategory_list,
            'centuries': centuries,
            'genre_list': genre_list,
            'random_films': get_random_films(),
            'random_cards': random_cards,
            'authors_by_types': get_random_authors_by_types(),
            'children_items': children_items,
            'silver_items': silver_items
        }
    )

