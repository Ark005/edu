from django.db import models
from django.urls import reverse


class Artgenre(models.Model):

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
        max_length=3000,
        verbose_name='текст_превью',
        blank=True,
        null=True
    )


    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('genre_detail',kwargs={'slug':self.slug})