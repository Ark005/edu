from django.http import HttpRequest,HttpResponse
from django.shortcuts import render
from django.views.generic import View,ListView
from ..models import Author, Category,Century


class CenturyDetailView(ListView):
    template_name = "core/century_details.html"

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        self.century = kwargs.get('slug')
        return super().get(request, *args, **kwargs)
    def get_queryset(self):
        queryset = Author.objects.filter(century__slug=self.century)
        return queryset

