from django.db import models
from core.models.author import Author
from core.models.singer import Singer
from core.utils.file import get_song_filepath, get_analysis_filepath, get_about_filepath
from django.dispatch import receiver
from django.urls import reverse
from django.db.models.signals import pre_save
from slugify import slugify


class Song(models.Model):

    slug = models.CharField(
        max_length=255,
        verbose_name='Ссылка',
        null=True,
        blank=True

    )
    author = models.ForeignKey(
        to=Author,
        on_delete=models.CASCADE,
        related_name='songs', # author.songs это то же самое что и Song.objects - то есть через аттрибут songs мы обращаемся к менеджеру класса Song 
        verbose_name='Автор'
    )
    duration = models.DurationField(
        max_length=255,
        verbose_name='Длительность',
        null=True,
        blank=True
    )
    name = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    singer = models.ForeignKey(
        to=Singer,
        on_delete=models.CASCADE,
        verbose_name='Исполнитель',
        null=True,
        blank=True
    )
    text = models.TextField(
        verbose_name='Текст произведения',
        null=True,
        blank=True
    )
    file = models.FileField(
        upload_to=get_song_filepath,
        verbose_name='Файл',
        null=True,
        blank=True
    )
    analysis = models.FileField(
        upload_to=get_analysis_filepath,
        verbose_name='Разбор',
        null=True,
        blank=True
    )
    about = models.FileField(
        upload_to=get_about_filepath,
        verbose_name='Рассказ об авторе',
        null=True,
        blank=True
    )
    @staticmethod
    def get_search_field():
        return 'name__icontains'
    

    def __str__(self):
        return f'{self.author} - {self.name}. Читает: {self.singer}'
    
    def get_absolute_url(self):
        return reverse('author_detail',kwargs={'slug':self.author.slug})

@receiver(pre_save, sender=Song)
def func_name(sender, instance: Song, **kwargs):
    slugname = slugify(instance.name)
    if instance.slug == None or instance.slug == '':
        instance.slug = slugname
        instance.save()

