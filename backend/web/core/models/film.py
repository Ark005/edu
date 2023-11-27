from django.db import models
from django.urls import reverse
from ..models import genre


class Film(models.Model):
    director = models.ForeignKey(
        'Author',
        related_name='films',
        on_delete=models.SET_NULL, 
        null=True)
    #author = models.ForeignKey(
        #'Author', 
        #on_delete=models.SET_NULL, 
        #null=True)
    genre = models.ManyToManyField(
        'Genre',
        related_name='films',
        blank=True)
    name = models.CharField(
        max_length=255,
        verbose_name='Название'
    )

    image = models.ImageField(
        upload_to='images',
        null=True,
        blank=True
    )
       
    slug = models.CharField(
        max_length=255,
        verbose_name='ссылка',
        null=True,
        unique=True

    )
    website = models.URLField(
        max_length=250,
        blank=True, 
        null=True
    )


    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f'{self.name}'
    
    def get_absolute_url(self):
        return reverse('film_detail',kwargs={'slug':self.slug})

    @staticmethod
    def get_search_field():
        return 'name__icontains'


    