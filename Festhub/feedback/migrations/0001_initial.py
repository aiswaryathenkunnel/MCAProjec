# Generated by Django 2.1 on 2018-11-19 11:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('studreg', '0002_studreg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_desc', models.CharField(default='', max_length=20)),
                ('feedback_date', models.DateField(default=datetime.date.today)),
                ('feedback_status', models.CharField(default='', max_length=10)),
                ('stud_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studreg.Studreg')),
            ],
        ),
    ]
