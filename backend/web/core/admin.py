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
    list_display = ('id', 'name', 'category', 'text_preview', 'get_type_display')
    ordering = ['type']
    prepopulated_fields = {"slug": ["name"]}
    list_display_links = ["name"]
    inlines = [VideoInLineAdmin, PictureInLineAdmin]
    search_fields = ['name']
    actions = ["set_category"]

    @admin.action(description="Назначить категории авторам")
    def set_category(self, request, qs):
        for q in qs:
            categ = Category.objects.filter(slug=q.type).first()
            q.category = categ
            q.save()
        self.message_user(
            request,
            "Для авторов были назначены категории"
        )

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
    list_display = ( 'name', 'type')
    prepopulated_fields = {"slug": ["name"]}



@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    pass
    prepopulated_fields = {"slug": ["name"]}


@admin.register(Century)
class CenturyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["display_name"]}


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    ordering = ['name']
    prepopulated_fields = {"slug": ["name"]}



@admin.register(CenturyDescription)
class CenturyDescriptionAdmin(admin.ModelAdmin):
    pass