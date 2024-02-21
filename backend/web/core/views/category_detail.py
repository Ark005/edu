from typing import Any
from django.db import models
from django.http import HttpRequest, HttpResponse
from ..models import Author, Category, Subcategory, Film, Century, CenturyDescription,Genre
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.shortcuts import redirect
from django.urls import reverse


class CategoryDetailView(ListView):
    template_name = "core/category.html"
    model = Author
    def get_queryset(self):
        return Genre.objects.filter(type=self.kwargs.get('slug'),parent__isnull=True)

    def get_context_data(self):
        context = super().get_context_data()
        context['subcategorylist'] = self.subcategorylist()
        context['centuries'] = self.centuries()
        return context

    def subcategorylist(self):
        queryset = Subcategory.objects.filter(category__slug=self.kwargs.get('slug'))
        return queryset

    def centuries(self):
        queryset = CenturyDescription.objects.filter(category__slug=self.kwargs.get("slug")).order_by("century__value")
        return queryset
