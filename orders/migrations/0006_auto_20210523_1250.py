# Generated by Django 3.1.2 on 2021-05-23 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20210523_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='d_id',
            field=models.ForeignKey(help_text='Код доставки', null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.delivery'),
        ),
    ]
