# Generated by Django 2.1.8 on 2019-04-16 04:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import server.pages.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_auto_20190415_0353'),
    ]

    operations = [
        migrations.CreateModel(
            name='OderItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('unit_price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('phone_no', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('sub_district', models.CharField(help_text='ตำบล', max_length=100)),
                ('district', models.CharField(help_text='อำเภอ', max_length=100)),
                ('province', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('unit_price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('discount_price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('image', models.ImageField(null=True, upload_to=server.pages.models.upload_helper)),
            ],
        ),
        migrations.AlterField(
            model_name='page',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updater', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Page'),
        ),
        migrations.AddField(
            model_name='order',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Page'),
        ),
        migrations.AddField(
            model_name='oderitems',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Order'),
        ),
        migrations.AddField(
            model_name='oderitems',
            name='product_variant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.ProductVariant'),
        ),
    ]
