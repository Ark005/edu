from django.db import models
from django.urls import reverse

class Century(models.Model):
    
    value = models.IntegerField(
        verbose_name='Век',
        unique=True,
        default=0,
        help_text='значение'

    )
    text = models.TextField(
        verbose_name='описание века',
        null=True,
        blank=True
    )

    display_name=models.CharField(
        max_length=255,
        verbose_name='Век',
        help_text='отображаемое значение'
    )
    

    slug = models.CharField(
        max_length=255,
        verbose_name='ссылка',
        null=True,
        unique=True
    )


    def __str__(self):
        return f'{self.display_name}'
    

    def get_absolute_url(self):
        return reverse('century_detail',kwargs={'slug':self.slug})
    
    class Meta:
        verbose_name_plural = "века"
        ordering=['value']
    
    @staticmethod
    def get_search_field():
        return 'display_name__icontains'
