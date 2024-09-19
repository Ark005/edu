from django.db import models
from django.urls import reverse


class SuperCategory(models.Model):
    slug = models.CharField(
        max_length=255,
        verbose_name='ссылка',
        null=True,
        unique=True
    )

    image = models.ImageField(
        upload_to='supercategory_images',
        null=True,
        blank=True
    )

    name = models.CharField(
        max_length=255,
        verbose_name='Имя'
    )

    description = models.CharField(
        max_length=500,
        verbose_name='Описание'
    )

    def get_absolute_url(self):
        return reverse('supercategory_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ["name"]
        verbose_name = 'Суперкатегория'
        verbose_name_plural = 'Суперкатегории'

    def __str__(self):
        return f'{self.name}'
