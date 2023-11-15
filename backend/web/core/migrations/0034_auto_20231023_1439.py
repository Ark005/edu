# Generated by Django 3.2.9 on 2023-10-23 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_category_preview_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='author',
            name='type',
            field=models.CharField(choices=[['music', 'Музыкант'], ['writer', 'Литератор'], ['artist', 'Художник'], ['philosopher', 'Философ'], ['musician', 'Музыкант'], ['lector', 'Лектор'], ['director', 'Режиссер']], max_length=255, null=True, verbose_name='тип'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(choices=[['music', 'Музыкант'], ['writer', 'Литератор'], ['artist', 'Художник'], ['philosopher', 'Философ'], ['musician', 'Музыкант'], ['lector', 'Лектор'], ['director', 'Режиссер']], max_length=300, null=True),
        ),
    ]
