from django.db import models
from django.urls import reverse

from core.models.author import author_type_choices


class Genre(models.Model):

    parent = models.ForeignKey('self',on_delete=models.CASCADE,related_name='children',null=True,blank=True)
    name = models.CharField(max_length=100)
    slug = models.CharField(
        max_length=255,
        verbose_name='ссылка',
        null=True,
        unique=True)
    image = models.ImageField(
        upload_to='images',
        null=True,
        blank=True
    )
    text_preview = models.TextField(
        max_length=5000,
        verbose_name='текст_превью',
        blank=True,
        null=True
    )
    type = models.CharField(
        max_length=100,
        verbose_name='тип жанра',
        blank=True,
        null=True,
        choices=author_type_choices
    )
    website = models.URLField(
        max_length=250,
        blank=True,
        null=True
    )


    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} - {self.get_type_display()}"
    
    def get_absolute_url(self):
        return reverse('genre_detail',kwargs={'slug':self.slug})