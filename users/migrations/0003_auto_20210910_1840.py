# Generated by Django 3.0 on 2021-09-10 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210909_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='dp',
            field=models.ImageField(default='/media/images/dp.png ', upload_to='images'),
        ),
    ]
