# Generated by Django 2.2.5 on 2019-12-03 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goodapp', '0004_auto_20191203_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='parent_catalog',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, to='goodapp.Good', verbose_name='Родительский каталог'),
        ),
    ]
