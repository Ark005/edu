from django.views import View
from django.views.generic import DetailView

from core.models import SuperCategory, Category


class SuperCategoryDetailView(DetailView):
    queryset = SuperCategory.objects.all()
    template_name = "core/supercategory.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['categories'] = Category.objects.filter(supercategory=self.get_object())
        return context

