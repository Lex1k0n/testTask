# Generated by Django 5.0.2 on 2024-03-01 13:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_productmodel_starttime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='starttime',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 1, 16, 56, 25, 829627)),
        ),
    ]
