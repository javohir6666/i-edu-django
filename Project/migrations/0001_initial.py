# Generated by Django 4.0.4 on 2022-05-12 12:59

import autoslug.fields
import ckeditor.fields
from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProjectName', models.CharField(max_length=500)),
                ('ProjectDesc', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to='img/projects/')),
                ('website', models.URLField(max_length=250)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='ProjectName')),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('seo_desc', models.TextField(default=ckeditor.fields.RichTextField(), max_length=50)),
                ('seo_keywords', models.TextField(default=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'))),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name_plural': 'Proyektlar',
            },
        ),
    ]
