from django.http import HttpRequest,HttpResponse
from django.shortcuts import render
from django.views.generic import View,ListView
from ..models import Author, Category, Century, century


class CenturyDetailView(ListView):
    template_name = "core/century_details.html"

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        self.century = kwargs.get('slug')
        return super().get(request, *args, **kwargs)
    def get_queryset(self):
        queryset = Category.objects.filter(subcategories__authors__century__slug=self.century).distinct()
        return queryset
    def get_context_data(self):
        context = super().get_context_data()
        context['century'] = Century.objects.filter(slug=self.century).first()
        return context


