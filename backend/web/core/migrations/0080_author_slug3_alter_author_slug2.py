# Generated by Django 4.2.7 on 2024-04-27 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0079_alter_author_slug2'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='slug3',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='слаг автора произведения'),
        ),
        migrations.AlterField(
            model_name='author',
            name='slug2',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='слаг произведения'),
        ),
    ]