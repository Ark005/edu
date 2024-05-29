from django.views.generic import CreateView
from django.conf import settings
from core.models import Feedback
import requests


def send_tg_message(message):
    url = f"https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage?chat_id={settings.ADMIN_CHAT_ID}&text={message}"
    requests.get(url)


class FeebackCreateView(CreateView):
    template_name = 'core/feedback.html'
    model = Feedback
    fields = ["name", "email", "message"]

    def get_success_url(self):
        return "/"

    def form_valid(self, form):
        response = super().form_valid(form)
        text = "Вы получили новое обращение\n"
        text += f"\nИмя: {form.cleaned_data.get('name')}"
        text += f"\nEmail: {form.cleaned_data.get('email')}"
        text += f"\nСообщение: {form.cleaned_data.get('message')}"
        send_tg_message(text)
        return response

