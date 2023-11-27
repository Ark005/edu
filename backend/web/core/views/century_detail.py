from django.http import HttpRequest,HttpResponse
from django.shortcuts import render
from django.views.generic import View,ListView
from ..models import Author


class CenturyDetailView(ListView):
    template_name = "core/century.html"

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        self.century = kwargs.get('century')
        return super().get(request, *args, **kwargs)
    def get_queryset(self):
        queryset = Author.objects.filter(century=self.century)
        return queryset
    


