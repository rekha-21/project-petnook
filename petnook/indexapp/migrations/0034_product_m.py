# Generated by Django 4.2.4 on 2023-09-25 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexapp', '0033_wishlist1'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='m',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
