# Generated by Django 4.2.4 on 2023-09-20 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('indexapp', '0018_petcategory_productsubcategory_delete_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productsubcategory',
            name='name',
        ),
        migrations.AddField(
            model_name='productsubcategory',
            name='sub_category',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default=None, max_length=100, null=True)),
                ('pet_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indexapp.petcategory')),
            ],
        ),
        migrations.AddField(
            model_name='productsubcategory',
            name='product_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='indexapp.productcategory'),
        ),
    ]
