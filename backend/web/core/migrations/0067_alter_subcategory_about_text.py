# Generated by Django 4.2.7 on 2024-02-10 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0066_subcategory_about_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='about_text',
            field=models.TextField(blank=True, max_length=3000, null=True, verbose_name='about'),
        ),
    ]
