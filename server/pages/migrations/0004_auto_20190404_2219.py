# Generated by Django 2.1.8 on 2019-04-04 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_page_product_size_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='product_image5',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='page',
            name='product_image6',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
