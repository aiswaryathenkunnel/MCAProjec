# Generated by Django 2.1 on 2018-11-11 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventreg', '0002_remove_eventreg_stud_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventreg',
            name='event_reg_no',
            field=models.BigIntegerField(),
        ),
    ]
