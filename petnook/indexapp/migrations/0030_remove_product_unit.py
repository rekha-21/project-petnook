# Generated by Django 4.2.4 on 2023-09-23 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indexapp', '0029_product_unit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='unit',
        ),
    ]
