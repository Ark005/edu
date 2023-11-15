# Generated by Django 3.2.9 on 2023-09-29 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(choices=[['music', 'Музыкант'], ['writer', 'Литератор'], ['artist', 'Художник'], ['philosopher', 'Философ'], ['director', 'Режиссер']], max_length=300, null=True),
        ),
    ]
