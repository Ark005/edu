from django.db import models
from core.models.author import Author
from core.models.singer import Singer
from core.utils.file import get_song_filepath, get_analysis_filepath, get_about_filepath
from django.dispatch import receiver
from django.urls import reverse
from django.db.models.signals import pre_save
from slugify import slugify

from core.utils.video import get_video_preview_link


class Video(models.Model):

    slug = models.CharField(
        max_length=255,
        verbose_name='Ссылка',
        null=True,
        blank=True

    )
    author = models.ForeignKey(
        to=Author,
        on_delete=models.CASCADE,
        related_name='videos', # author.songs это то же самое что и Song.objects - то есть через аттрибут songs мы обращаемся к менеджеру класса Song
        verbose_name='Автор'
    )
    name = models.CharField(
        max_length=255,
        verbose_name='Название'

    )

    def get_preview_image(self):
        return get_video_preview_link(self.slug)


    def get_absolute_url(self):
        return reverse('author_detail', kwargs={'slug': self.author.slug})

    @staticmethod
    def get_search_field():
        return 'name__icontains'
    

    def __str__(self):
        return f'{self.author} - {self.name}'
    



