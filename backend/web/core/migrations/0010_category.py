# Generated by Django 3.2.9 on 2023-09-26 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_author_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('is_primary', models.BooleanField(default=False)),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='image')),
                ('preview_text', models.TextField(blank=True, max_length=60, null=True, verbose_name='Preview Text')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='core.category')),
            ],
            options={
                'verbose_name_plural': 'Категории',
            },
        ),
    ]
