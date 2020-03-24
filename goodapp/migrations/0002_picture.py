# Generated by Django 2.2.5 on 2019-12-03 12:18

from django.db import migrations, models
import django.db.models.deletion
import goodapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('goodapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, verbose_name='Наименование')),
                ('slug', models.SlugField(blank=True, max_length=10, verbose_name='Url')),
                ('image270', models.ImageField(blank=True, default=None, null=True, upload_to=goodapp.models.get_image_name_270, verbose_name='Изображение 270x301')),
                ('image420', models.ImageField(blank=True, default=None, null=True, upload_to=goodapp.models.get_image_name_570, verbose_name='Изображение 570x570')),
                ('image1000', models.ImageField(blank=True, default=None, null=True, upload_to=goodapp.models.get_image_name_1200, verbose_name='Изображение 1200x1125')),
                ('image174', models.ImageField(blank=True, default=None, null=True, upload_to=goodapp.models.get_image_name_90, verbose_name='Изображение 90x90')),
                ('main_image', models.BooleanField(default=False, verbose_name='Основная картинка')),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goodapp.Good', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Картинка',
                'verbose_name_plural': 'Картинки',
            },
        ),
    ]
