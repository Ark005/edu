from django.db import models
from django.urls import reverse
from core.models.author import author_type_choices


class CenturyDescription(models.Model):

    type = models.CharField(
        max_length=100,
        verbose_name='тип жанра',
        blank=True,
        null=True,
        choices=author_type_choices
    )
    text = models.TextField(
        verbose_name='описание века',
        null=True,
        blank=True
    )
    detailed_text = models.TextField(
        verbose_name='детальное описание',
        null=True,
        blank=True
    )
    rel_changes_text = models.TextField(
        verbose_name='религиозные изменения',
        null=True,
        blank=True
    )
    mistake_text = models.TextField(
        verbose_name='описание ошибок',
        null=True,
        blank=True
    )
    category = models.ForeignKey(
        to='Category',
        blank=True,
        null=True,
        on_delete=models.PROTECT
    )
    century = models.ForeignKey(
        to='Century',
        blank=True,
        null=True,
        on_delete=models.PROTECT
    )

    def get_absolute_url(self):
        return reverse('category_century_detail', kwargs={'century': self.century.slug, 'category': self.category.slug})
