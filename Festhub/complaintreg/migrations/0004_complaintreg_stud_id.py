# Generated by Django 2.1 on 2018-11-19 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaintreg', '0003_remove_complaintreg_stud_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaintreg',
            name='stud_id',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
    ]