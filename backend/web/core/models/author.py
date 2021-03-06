from django.db import models

from django.urls import reverse

def get_century_choices():

    century_choices = []
    for century in range(-1, 22):
        if century<0:
            x = f'{abs(century)} до н.э.'
        elif century == 0:
            continue
        else:
            x = f'{century}'
        century_choices.append([century,x])
    return century_choices

class TypeChoices:
        MUSIC='music'
        WRITER='writer'
        ARTIST='artist'
        PHILOSOPHER='philosopher'
        MUSICIAN='musician'
        DIRECTOR='director'
        LECTOR='lector'
        SPIRITUAL='spiritual'
        

author_type_choices = [
            [TypeChoices.MUSIC,'Музыкант'],
            [TypeChoices.WRITER,'Литератор'],
            [TypeChoices.ARTIST,'Художник'],
            [TypeChoices.PHILOSOPHER,'Философ'],
            [TypeChoices.MUSICIAN,'Музыкант'],
            [TypeChoices.LECTOR,'Лектор'],
            [TypeChoices.DIRECTOR,'Режиссер'],
            [TypeChoices.SPIRITUAL,'Духоносный'],
            ]

class TypeCenturyChoices:
        SILVER='silver'
        GOLD='gold'
        
century_type_choices = [
            [TypeCenturyChoices.SILVER,'Серебряный'],
            [TypeCenturyChoices.GOLD,'Золотой'],
            ]


class Author(models.Model):
    
    name = models.CharField(
        max_length=255,
        verbose_name='Имя'
    )
        #dob = models.TextField(
        #date = models.DateTimeField(default=datetime.now, blank=True)
        #verbose_name='дата',
        #blank=True, 
        #null=True
    #)
    
    text = models.TextField(
        max_length=80000,
        verbose_name='текст',
        blank=True, 
        null=True
    )

    website = models.URLField(
        max_length=250,
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
    def __str__(self):
        return f'{self.name}'
    

    def get_absolute_url(self):
        return reverse('author_detail',kwargs={'slug':self.slug})
    
    class Meta:
        #verbose_name_plural = "Категории"
        ordering=['century']
    
    @staticmethod
    def get_search_field():
        return 'name__icontains'
    
    teacher = models.ManyToManyField(
        to="self",
        related_name='students',
        blank=True,
    )
    antagonist = models.ManyToManyField(
        to="self",related_name='antagonist',
        blank=True,
    )
    
    associate = models.ManyToManyField(
        to="self",related_name='associate',
        blank=True,
    )

    student = models.ManyToManyField(
        to="self",related_name='student',

        blank=True,
    )
    class Meta:
        ordering = ["name"]
    