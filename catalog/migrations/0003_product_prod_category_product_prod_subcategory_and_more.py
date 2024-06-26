# Generated by Django 5.0.3 on 2024-04-02 22:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_remove_product_prod_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='prod_category',
            field=models.CharField(default=111, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='prod_subcategory',
            field=models.CharField(default=222, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='prod_subcategory_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='catalog.subcategory', verbose_name='Подкатегория'),
        ),
    ]
