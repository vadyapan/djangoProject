# Generated by Django 4.1.3 on 2022-11-29 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_rename_total_price_order_order_total_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_total_price',
            new_name='total_price',
        ),
    ]