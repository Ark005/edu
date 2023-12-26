from django.contrib import admin
from django.contrib.admin import TabularInline, StackedInline
from .models import *


class VideoInLineAdmin(TabularInline):
    model = Video


class PictureInLineAdmin(StackedInline):
    model = Picture


# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'text_preview', 'get_type_display')
    ordering = ['type']
    prepopulated_fields = {"slug": ["name"]}
    list_display_links = ["name"]
    inlines = [VideoInLineAdmin, PictureInLineAdmin]
    search_fields = ['name']


@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    pass
    prepopulated_fields = {"slug": ["name"]}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
    # prepopulated_fields={"slug": ["name"]}


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}


# class AuthorInstanceAdmin(admin.ModelAdmin):
# list_filter = ('name', 'century')

@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    pass
    prepopulated_fields = {"slug": ["name"]}


@admin.register(Century)
class CenturyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["display_name"]}


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}
