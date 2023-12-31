# Generated by Django 4.2.4 on 2023-09-20 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('indexapp', '0017_wishlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='PetCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSubcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pet_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indexapp.petcategory')),
            ],
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
