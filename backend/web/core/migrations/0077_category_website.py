# Generated by Django 4.2.7 on 2024-04-11 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0076_centurydescription_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='website',
            field=models.URLField(blank=True, max_length=250, null=True),
        ),
    ]
