from django.urls import path
from core import views
from django.views.generic import TemplateView

urlpatterns = [

    path('', views.index_view),
    path('category/<str:slug>', views.CategoryDetailView.as_view(), name="category_detail"),
    path('century/<str:slug>', views.CenturyDetailView.as_view(), name="century_detail"),
    path('<str:slug>/detail', views.author_detail_view, name="author_detail"),
    path('genre/<str:slug>/detail', views.GenreDetailView.as_view(), name="genre_detail"),
    path('genre/list', views.genre_list_view, name="genre_list"),
    path('author/list', views.author_list_view),
    #path('film/list', views.film_list_view),
    path('film/<str:slug>/detail', views.FilmDetailView.as_view(), name="film_detail"),
    # path('author/<str:slug>/detail', views.AuthorDetail.as_view(), name="author_detail"),
    path('search', views.SearchView.as_view()),
    # path('<str:slug>/detail', views.category_detail, name="category_detail"),
    path('century/<str:century>/category/<str:category>', views.CenturyCategoryDetailView.as_view(),
         name="category_century_detail"),


]
