# Generated by Django 3.1.5 on 2021-01-21 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210121_0523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='expiration_date',
        ),
        migrations.RemoveField(
            model_name='product',
            name='mfg_date',
        ),
    ]