# Generated by Django 3.0 on 2021-09-09 15:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20210909_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 9, 15, 5, 49, 902131)),
        ),
    ]
