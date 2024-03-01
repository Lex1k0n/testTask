# Generated by Django 5.0.2 on 2024-03-01 15:34

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_productmodel_starttime'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='group_count',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='max_part',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='min_part',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='starttime',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 1, 18, 34, 17, 168560)),
        ),
        migrations.CreateModel(
            name='GroupModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productmodel')),
            ],
        ),
        migrations.CreateModel(
            name='GroupMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.groupmodel')),
            ],
        ),
        migrations.CreateModel(
            name='LessonModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('ref', models.URLField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productmodel')),
            ],
        ),
    ]