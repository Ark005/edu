# Generated by Django 3.2.9 on 2023-10-31 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='singer',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='Текст произведения'),
        ),
    ]
