# Generated by Django 4.2.5 on 2024-02-29 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductModel',
            new_name='Product',
        ),
    ]
