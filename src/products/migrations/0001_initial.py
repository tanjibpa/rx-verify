# Generated by Django 3.1.5 on 2021-01-21 05:22

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('updated_by', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('name', models.CharField(max_length=100)),
                ('mfg_date', models.DateField()),
                ('expiration_date', models.DateField()),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'products',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='RawMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('updated_by', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Raw Material',
                'verbose_name_plural': 'Raw Materials',
                'db_table': 'raw_materials',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='ProductBatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('updated_by', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('batch_number', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('mfg_date', models.DateField()),
                ('expiration_date', models.DateField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'verbose_name': 'Product Batch',
                'verbose_name_plural': 'Product Batches',
                'db_table': 'product_batches',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.AddField(
            model_name='product',
            name='raw_materials',
            field=models.ManyToManyField(to='products.RawMaterial'),
        ),
    ]
