# Generated by Django 3.2.9 on 2023-10-20 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_auto_20231020_0814'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='preview_text',
            field=models.TextField(blank=True, max_length=60, null=True, verbose_name='Preview Text'),
        ),
    ]
