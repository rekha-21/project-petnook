# Generated by Django 4.2.4 on 2023-09-20 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indexapp', '0020_rename_productsubcategory_catsubcategory_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catsubcategory',
            name='pet_category',
        ),
        migrations.RemoveField(
            model_name='dogsubcategory',
            name='pet_category',
        ),
    ]
