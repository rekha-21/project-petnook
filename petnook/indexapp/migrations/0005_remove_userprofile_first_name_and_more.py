# Generated by Django 4.2.4 on 2023-09-11 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indexapp', '0004_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='last_name',
        ),
    ]
