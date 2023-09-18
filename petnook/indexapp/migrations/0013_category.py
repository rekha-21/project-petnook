# Generated by Django 4.2.4 on 2023-09-14 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexapp', '0012_delete_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet', models.CharField(choices=[('dog', 'Dog'), ('cat', 'Cat'), ('bird', 'Bird')], max_length=10)),
                ('category_name', models.CharField(max_length=255)),
                ('subcategory1', models.CharField(max_length=255)),
                ('subcategory2', models.CharField(max_length=255)),
                ('subcategory3', models.CharField(max_length=255)),
                ('subcategory4', models.CharField(max_length=255)),
            ],
        ),
    ]