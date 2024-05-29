from django.db import models
from core.models.author import Author
from core.models.singer import Singer
from core.utils.file import get_song_filepath, get_analysis_filepath, get_about_filepath
from django.dispatch import receiver
from django.urls import reverse
from django.db.models.signals import pre_save
from slugify import slugify


class Feedback(models.Model):
    email = models.CharField(
        max_length=255,
        verbose_name='Ссылка',
        null=True,
        blank=True
    )
    message = models.TextField(
        verbose_name='Название'
    )
    name = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    created_date = models.DateTimeField(
        verbose_name='Дата создания сообщения',
        auto_now_add=True
    )

    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return f'{self.name}'
