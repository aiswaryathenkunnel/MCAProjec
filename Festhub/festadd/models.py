from django.db import models
from datetime import date
from depttype.models import Depttype


class Festadd(models.Model):
    fest_name = models.CharField(max_length=30, default='')
    fest_theme = models.CharField(max_length=50, default='')
    clg_id = models.BigIntegerField()
    dept_id = models.ForeignKey(Depttype, on_delete=models.CASCADE)
    fest_date = models.DateField(default=date.today)
    fest_type = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.fest_name