from django.db import models
from django.dispatch import receiver
from django.urls import reverse
from django.db.models.signals import pre_save
from .century import Century


def get_century_choices():
    century_choices = []
    for century in range(-6, 22):
        if century < 0:
            x = f'{abs(century)} до н.э.'
        elif century == 0:
            continue
        else:
            x = f'{century}'
        century_choices.append([century, x])
    return century_choices


class TypeChoices:
    MUSIC = 'music'
    WRITER = 'writer'
    ARTIST = 'artist'
    PHILOSOPHER = 'philosopher'
    MUSICIAN = 'musician'
    DIRECTOR = 'director'
    LECTOR = 'lector'
    SPIRITUAL = 'spiritual'


author_type_choices = [
    [TypeChoices.MUSIC, 'Музыкант'],
    [TypeChoices.WRITER, 'Литератор'],
    [TypeChoices.ARTIST, 'Художник'],
    [TypeChoices.PHILOSOPHER, 'Философ'],
    [TypeChoices.LECTOR, 'Лектор'],
    [TypeChoices.DIRECTOR, 'Режиссер'],
    [TypeChoices.SPIRITUAL, 'Духоносный'],
]


def get_category_name_by_type(name: str) -> str:
    return list(filter(lambda item: item[0] == name, author_type_choices))[0][1]


class Author(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Имя'
    )
    creation_author = models.ForeignKey(
        to="self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Автор произведения",
        related_name="creations"
    )

    category = models.ForeignKey(
        to='Category',
        related_name='authors',
        blank=True,
        null=True,
        on_delete=models.PROTECT
    )

    subcategory = models.ManyToManyField(
        to='Subcategory',
        related_name='authors',
        blank=True,
    )

    text = models.TextField(
        max_length=80000,
        verbose_name='текст',
        blank=True,
        null=True
    )
    year = models.IntegerField(
        verbose_name='год рождения',
        blank=True,
        null=True
    )

    text_preview = models.TextField(
        max_length=3000,
        verbose_name='текст_превью',
        blank=True,
        null=True
    )
    slug = models.CharField(
        max_length=255,
        verbose_name='ссылка',
        null=True,
        unique=True
    )
    slug2 = models.CharField(
        max_length=255,
        verbose_name='слаг автора',
        null=True,
        blank=True
    )
    slug3 = models.CharField(
        max_length=255,
        verbose_name='имя автора произведения',
        null=True,
        blank=True
    )
    type = models.CharField(
        choices=author_type_choices,
        max_length=255,
        verbose_name='тип',
        null=True,

    )

    image = models.ImageField(
        upload_to='images',
        null=True,
        blank=True
    )

    century = models.ForeignKey(
        to='Century',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    genre = models.ManyToManyField(
        'Genre',
        related_name='authors',
        blank=True
    )
    last_name = models.CharField(
        max_length=1024,
        null=True,
        blank=True,
        verbose_name="Фамилия"
    )

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('author_detail', kwargs={'slug': self.slug})

    class Meta:
        # verbose_name_plural = "Категории"
        # ordering = ['century']
        ordering = ["name"]

    @staticmethod
    def get_search_field():
        return 'name__icontains'

    teacher = models.ManyToManyField(
        to="self",
        blank=True,
    )
    antagonist = models.ManyToManyField(
        to="self",
        blank=True,
    )

    associate = models.ManyToManyField(
        to="self",
        blank=True,
    )

    student = models.ManyToManyField(
        to="self",

        blank=True,
    )

    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")


@receiver(pre_save, sender=Author)
def func_name(sender, instance: Author, save=None, **kwargs):
    if instance.year is None:
        return
    if instance.year > 0:
        century = instance.year / 100 + 1
    else:
        century = instance.year / 100 - 1
    x = Century.objects.filter(value=century).first()
    instance.century = x
