# Generated by Django 4.2.5 on 2024-02-29 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('start_date', models.DateField()),
            ],
        ),
    ]
