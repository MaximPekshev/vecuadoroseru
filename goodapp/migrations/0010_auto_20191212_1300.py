# Generated by Django 2.2.5 on 2019-12-12 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goodapp', '0009_auto_20191205_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='description',
            field=models.TextField(blank=True, max_length=1024, verbose_name='Описание'),
        ),
    ]
