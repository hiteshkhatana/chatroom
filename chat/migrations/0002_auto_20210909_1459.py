# Generated by Django 3.0 on 2021-09-09 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='date',
            field=models.DateTimeField(auto_created=True),
        ),
    ]
