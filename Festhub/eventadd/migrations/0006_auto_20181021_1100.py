# Generated by Django 2.1 on 2018-10-21 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventadd', '0005_auto_20181021_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventadd',
            name='time_from',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='eventadd',
            name='time_to',
            field=models.TimeField(),
        ),
    ]
