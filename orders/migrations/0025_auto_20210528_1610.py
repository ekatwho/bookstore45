# Generated by Django 3.1.2 on 2021-05-28 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0024_auto_20210528_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False, verbose_name='Оплачено'),
        ),
    ]
