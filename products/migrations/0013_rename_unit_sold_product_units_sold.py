# Generated by Django 3.2 on 2022-03-10 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20220310_1755'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='unit_sold',
            new_name='units_sold',
        ),
    ]