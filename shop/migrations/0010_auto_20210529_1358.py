# Generated by Django 3.1.2 on 2021-05-29 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_remove_product_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor',
            old_name='id',
            new_name='v_id',
        ),
        migrations.AddField(
            model_name='product',
            name='v_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.vendor'),
        ),
    ]
