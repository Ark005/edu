# Generated by Django 3.2.9 on 2023-09-29 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_author_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
