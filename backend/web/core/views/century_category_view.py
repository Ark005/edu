from django.views.generic import ListView
from core.models import Author,CenturyDescription,Century


class CenturyCategoryDetailView(ListView):
    template_name = "core/century_category_detail.html"

    def get_queryset(self):
        authors = Author.objects.filter(century__slug=self.kwargs.get('century'), category__slug=self.kwargs.get('category')).order_by('last_name')
        return authors

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['description'] = self.get_description()
        context['century'] = self.get_century()
        return context

    def get_description(self):
        century_description = CenturyDescription.objects.filter(century__slug=self.kwargs.get('century'), category__slug=self.kwargs.get('category')).first()
        return century_description

    def get_century(self):
        century = Century.objects.filter(slug=self.kwargs.get('century')).first()
        return century
