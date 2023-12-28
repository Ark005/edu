from django.db import models
from django.urls import reverse


class CenturyDescription(models.Model):

    text = models.TextField(
        verbose_name='описание века',
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
