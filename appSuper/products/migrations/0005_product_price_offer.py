# Generated by Django 3.1.1 on 2020-09-23 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200914_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_offer',
            field=models.FloatField(null=True),
        ),
    ]
