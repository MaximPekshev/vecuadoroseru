# Generated by Django 2.2.5 on 2019-12-11 07:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goodapp', '0009_auto_20191205_1435'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summ', models.DecimalField(blank=True, decimal_places=0, default=0, editable=False, max_digits=15, verbose_name='Сумма заказа')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart_Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=0, max_digits=15)),
                ('price', models.DecimalField(decimal_places=0, max_digits=15)),
                ('summ', models.DecimalField(decimal_places=0, max_digits=15)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cartapp.Cart')),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='goodapp.Good')),
            ],
        ),
    ]