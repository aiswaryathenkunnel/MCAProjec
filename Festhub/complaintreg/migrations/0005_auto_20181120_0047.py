# Generated by Django 2.1 on 2018-11-19 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaintreg', '0004_complaintreg_stud_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaintreg',
            name='comp_reply',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='complaintreg',
            name='comp_status',
            field=models.CharField(default='', max_length=30),
        ),
    ]
