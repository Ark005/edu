# Generated by Django 4.2.7 on 2024-05-15 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_author_creation_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='creation_author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creations', to='core.author', verbose_name='Автор произведения'),
        ),
    ]
