
from django.db import models
from django.urls import reverse

class Subcategory(models.Model):

    category = models.ForeignKey(
        to='Category',
        on_delete=models.SET_NULL,
        related_name='subcategories',
        null=True,
        blank=True,
    )

    name = models.CharField(
        max_length=300
    )
    #main_image = models.ImageField(
       # upload_to='image',
        #blank=True,
        #null=True
   # )

    slug = models.CharField(
        max_length=300,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Cубкатегории"


