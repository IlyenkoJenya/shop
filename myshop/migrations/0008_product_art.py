# Generated by Django 3.2.9 on 2022-11-12 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0007_auto_20221108_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='art',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]
