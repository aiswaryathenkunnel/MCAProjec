# Generated by Django 2.1 on 2018-10-21 08:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festadd', '0009_auto_20181021_0654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='festadd',
            name='fest_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
