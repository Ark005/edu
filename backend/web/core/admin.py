from django.contrib import admin
from django.contrib.admin import TabularInline, StackedInline
from .models import *
from .models.author import TypeChoices


class BookInLineAdmin(TabularInline):
    model = Book


class VideoInLineAdmin(TabularInline):
    model = Video


class PictureInLineAdmin(StackedInline):
    model = Picture


class CreationInline(TabularInline):
    model = Author
    fields = ("name", "slug")


# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    change_form_template = "admin/select2_admin_form.html"
    list_display = ('id', 'name', 'category', 'text_preview', 'get_type_display')
    ordering = ['type']
    prepopulated_fields = {"slug": ["name"]}
    list_display_links = ["name"]
    inlines = [VideoInLineAdmin, PictureInLineAdmin, BookInLineAdmin, CreationInline]
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
    search_fields = ['name']

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    search_fields = ['name', 'created_date']

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    change_form_template = "admin/select2_admin_form.html"
    prepopulated_fields = {"slug": ["name"]}
    search_field = ['author']
    ordering = ['type']
    list_display = ('name', 'type')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
    # prepopulated_fields={"slug": ["name"]}

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}
    search_fields = ['name']


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    pass
    prepopulated_fields = {"slug": ["name"]}
    search_fields = ['name']


@admin.register(Century)
class CenturyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["display_name"]}


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    ordering = ['name']
    prepopulated_fields = {"slug": ["name"]}


@admin.register(CenturyDescription)
class CenturyDescriptionAdmin(admin.ModelAdmin):
    list_display = ['century', 'type']
    ordering = ['type']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'type')
    prepopulated_fields = {"slug": ["name"]}
    ordering = ['name']
