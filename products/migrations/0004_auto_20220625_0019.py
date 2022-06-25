# Generated by Django 3.2 on 2022-06-24 23:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_publication_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='isbn',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Please enter a valid ISBN', regex='$=^\\d{9}[\\d|X]$')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='isbn13',
            field=models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(message='Please enter a valid ISBN13', regex='$=^\\d{13}$')]),
        ),
    ]