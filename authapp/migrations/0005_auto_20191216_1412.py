# Generated by Django 2.2.5 on 2019-12-16 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_auto_20191216_1411'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buyer',
            old_name='с',
            new_name='name',
        ),
    ]
