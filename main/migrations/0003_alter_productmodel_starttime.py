# Generated by Django 5.0.2 on 2024-03-01 09:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_productmodel_author_productmodel_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='starttime',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 1, 12, 13, 47, 879755)),
        ),
    ]
