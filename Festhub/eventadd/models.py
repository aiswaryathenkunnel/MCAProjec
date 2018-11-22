from django.db import models
from festadd.models import Festadd


class Eventadd(models.Model):
    clg_id = models.BigIntegerField()
    fest_id = models.ForeignKey(Festadd, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=30, default='')
    event_desc = models.CharField(max_length=50, default='')
    event_fees = models.BigIntegerField()
    part_type = models.CharField(max_length=10, default='')
    max_part = models.BigIntegerField()
    time_from = models.CharField(max_length=6, default='')
    time_to = models.CharField(max_length=6, default='')
    venue = models.CharField(max_length=30, default="")

    def __str__(self):
        return self.event_name
