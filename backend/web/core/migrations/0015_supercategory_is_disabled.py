# Generated by Django 4.2.7 on 2024-09-25 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_supercategory_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='supercategory',
            name='is_disabled',
            field=models.BooleanField(default=False, verbose_name='Раздел выключен'),
        ),
    ]
