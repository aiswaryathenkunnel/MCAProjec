# Generated by Django 2.1 on 2018-11-11 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventreg', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventreg',
            name='stud_id',
        ),
    ]
