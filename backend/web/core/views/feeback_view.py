from django.views.generic import CreateView

from core.models import Feedback


class FeebackCreateView(CreateView):
    template_name = 'core/feedback.html'
    model = Feedback
    fields = ["name", "email", "message"]

    def get_success_url(self):
        return "/"
