# Generated by Django 3.0.6 on 2020-10-14 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20201014_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='discount_price',
            field=models.FloatField(default=0.0),
        ),
    ]
