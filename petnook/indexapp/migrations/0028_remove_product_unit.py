# Generated by Django 4.2.4 on 2023-09-23 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indexapp', '0027_remove_product_priceunit_product_unit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='unit',
        ),
    ]
