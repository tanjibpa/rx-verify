# Generated by Django 3.1.5 on 2021-01-23 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='approved',
        ),
        migrations.AddField(
            model_name='productbatch',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
