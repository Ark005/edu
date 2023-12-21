from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from .settings2 import MEDIA_DIR, MEDIA_URL
from django.views.generic import TemplateView
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('about.html/', TemplateView.as_view(template_name="core/about.html")),
    path(r'^favicon\.ico$', RedirectView.as_view(url='/media/images/favicon.ico'), name='favicon')
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_DIR)


