# Generated by Django 4.2.4 on 2023-09-22 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexapp', '0024_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petcategory',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
