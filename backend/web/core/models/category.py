from django.db import models
from core.models.author import author_type_choices
from django.urls import reverse

class Category(models.Model):
    parent = models.ForeignKey(
        to='self',
        on_delete=models.CASCADE,
        related_name='subcategories',
        null=True,
        blank=True
    )
    name = models.CharField(
        max_length=300
    )
    is_primary = models.BooleanField(
        default=False
    )
    main_image = models.ImageField(
        upload_to='image',
        blank=True,
        null=True
    )
    about_text = models.TextField(
        max_length= 300,
        verbose_name='about',
        blank=True, 
        null=True
    )
    
    slug = models.CharField(
        max_length=300,
        null=True,
        choices=author_type_choices
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Категории"

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})
    
