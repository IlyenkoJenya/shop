# Generated by Django 3.2.9 on 2022-11-12 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0008_product_art'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='art',
            new_name='artikul',
        ),
    ]
