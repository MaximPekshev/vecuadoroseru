# Generated by Django 2.2.5 on 2019-12-05 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goodapp', '0007_auto_20191204_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='old_price',
            field=models.DecimalField(blank=True, decimal_places=0, default='0', max_digits=15, verbose_name='Цена'),
        ),
    ]