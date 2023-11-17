# Generated by Django 4.2.7 on 2023-11-17 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0046_century_remove_author_century_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='century',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.century'),
        ),
    ]
