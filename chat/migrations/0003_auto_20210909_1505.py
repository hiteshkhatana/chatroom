# Generated by Django 3.0 on 2021-09-09 15:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20210909_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 9, 15, 5, 38, 851804)),
        ),
    ]
