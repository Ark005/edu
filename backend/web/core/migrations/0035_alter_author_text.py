# Generated by Django 3.2.9 on 2023-10-24 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_auto_20231023_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='text',
            field=models.TextField(blank=True, max_length=80000, null=True, verbose_name='текст'),
        ),
    ]
