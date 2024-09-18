from django.urls import path
from core import views
from django.views.generic import TemplateView

from core.sitemap import AuthorSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    "author": AuthorSitemap,
}

urlpatterns = [

    path('', views.index_view),
    path('category/<str:slug>', views.CategoryDetailView.as_view(), name="category_detail"),
    path('century/<str:slug>', views.CenturyDetailView.as_view(), name="century_detail"),
    path('<str:slug>/detail', views.author_detail_view, name="author_detail"),
    path('genre/<str:slug>/detail', views.GenreDetailView.as_view(), name="genre_detail"),
    path('genre/list', views.genre_list_view, name="genre_list"),
    path('author/list', views.author_list_view),
    path('film/list', views.film_list_view),
    path('film/<str:slug>/detail', views.FilmDetailView.as_view(), name="film_detail"),
    path('search', views.SearchView.as_view()),
    path('century/<str:century>/category/<str:category>', views.CenturyCategoryDetailView.as_view(),
         name="category_century_detail"),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
    path('feedback/create', views.FeebackCreateView.as_view(), name="feedback_create"),
    path('supercategory/<str:slug>', views.SuperCategoryDetailView.as_view(), name="supercategory_detail"),
]
