from django.db import models
from eventadd.models import Eventadd


class Eventreg(models.Model):
    event_id = models.ForeignKey(Eventadd, on_delete=models.CASCADE)
    event_reg_no = models.BigIntegerField()
    payment_status = models.CharField(max_length=5, default='')

    def __str__(self):
        return self.event_id

