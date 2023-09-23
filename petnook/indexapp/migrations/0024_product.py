# Generated by Django 4.2.4 on 2023-09-22 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('indexapp', '0023_remove_wishlist_products_remove_wishlist_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('brand_name', models.CharField(blank=True, max_length=255, null=True)),
                ('num_items', models.PositiveIntegerField()),
                ('quantity_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image1', models.ImageField(upload_to='product_images/')),
                ('image2', models.ImageField(upload_to='product_images/')),
                ('image3', models.ImageField(upload_to='product_images/')),
                ('pet_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indexapp.petcategory')),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indexapp.productcategory')),
                ('product_subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indexapp.productsubcategory')),
            ],
        ),
    ]
