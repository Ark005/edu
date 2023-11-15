from django.contrib import admin
from .models import Author,Singer,Song,Category,Genre,Film,Picture

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=('id','name','text_preview','get_type_display','century_type')
    list_editable=['century_type']
    ordering=['type']
    prepopulated_fields={"slug": ["name"]}
    list_display_links=["name"]
@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug": ["name"]}

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    pass
    prepopulated_fields={"slug": ["name"]}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
    #prepopulated_fields={"slug": ["name"]}
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug": ["name"]}

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug": ["name"]}
#class AuthorInstanceAdmin(admin.ModelAdmin):
    #list_filter = ('name', 'century')

@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    pass
    prepopulated_fields={"slug": ["name"]}