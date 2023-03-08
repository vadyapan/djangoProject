# Generated by Django 4.1.4 on 2023-01-18 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_remove_product_specifications'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='camera',
            new_name='spec_1',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='connection',
            new_name='spec_2',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='display',
            new_name='spec_3',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='equipment',
            new_name='spec_4',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='processor',
            new_name='spec_5',
        ),
    ]