# Generated by Django 4.2.7 on 2023-11-12 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0042_author_website_alter_author_antagonist_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='website',
            field=models.URLField(blank=True, max_length=250, null=True),
        ),
    ]
