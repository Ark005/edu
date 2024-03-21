from django.db import models


class Singer(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Имя'
    )
    slug = models.CharField(
        max_length=255,
        verbose_name='ссылка',
        null=True,
        unique=True
    )
    text = models.TextField(
        verbose_name='Текст произведения',
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.name}'


