# Generated by Django 3.1.2 on 2021-05-25 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_remove_order_d_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('p_id', models.AutoField(default=1, help_text='Код доставки', primary_key=True, serialize=False)),
                ('p_type', models.CharField(max_length=50)),
            ],
        )

    ]
