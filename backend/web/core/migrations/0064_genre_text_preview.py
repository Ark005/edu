# Generated by Django 4.2.7 on 2024-02-05 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0063_rename_rel_changes_text_centurydescription_rel_changes_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='text_preview',
            field=models.TextField(blank=True, max_length=3000, null=True, verbose_name='текст_превью'),
        ),
    ]