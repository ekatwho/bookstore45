# Generated by Django 3.1.2 on 2021-05-23 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20210504_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ord_check_time',
            field=models.DateTimeField(help_text='Дата оформления', null=True, verbose_name='Оформлено'),
        ),
        migrations.AddField(
            model_name='order',
            name='ord_del_time',
            field=models.DateTimeField(help_text='Дата доставки', null=True, verbose_name='Доставлено'),
        ),
    ]
