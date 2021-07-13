# Generated by Django 3.0.6 on 2021-06-23 19:23

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20210623_2134'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Контент')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Creation time')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='Update time')),
            ],
            options={
                'verbose_name': 'Новости',
                'verbose_name_plural': 'Новости',
                'ordering': ['-update_time', '-id'],
            },
        ),
    ]
