# Generated by Django 3.1.2 on 2021-05-26 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20210526_1213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery',
            name='d_id',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='p_id',
        ),
        migrations.AddField(
            model_name='delivery',
            name='id',
            field=models.AutoField(auto_created=True, default='', primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='id',
            field=models.AutoField(auto_created=True, default='', primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='o_id',
            field=models.AutoField(help_text='Код Заказа', primary_key=True, serialize=False),
        ),
    ]
