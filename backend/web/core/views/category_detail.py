from typing import Any
from django.db import models
from django.http import HttpRequest, HttpResponse
from ..models import Author,Category
from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView 
from django.shortcuts import redirect
from django.urls import reverse
#from django.utils.text import slugify
# /genre/list - это путь до списка жанров. Чтобы получить этот путь по имени, можно использовать 
# функцию reverse

class CategoryDetailView(ListView):
    template_name = "core/category.html"
    model = Author
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        self.category_slug = kwargs.get('slug')
        if self.category_slug == 'director':
           return redirect(reverse('genre_list'))
        return super().get(request, *args, **kwargs)
    def get_queryset(self):
        queryset = Author.objects.filter(type=self.category_slug).order_by('century')
        return queryset
    def get_context_data(self):
        context = super().get_context_data()
        return context

    
    
    
    
   
    
