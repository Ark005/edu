# Generated by Django 3.2.9 on 2023-10-19 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_author_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='text',
            field=models.TextField(blank=True, max_length=20000, null=True, verbose_name='текст'),
        ),
    ]
