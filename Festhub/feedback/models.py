from django.db import models
from datetime import date


class Feedback(models.Model):
    stud_id = models.BigIntegerField()
    feedback_desc = models.CharField(max_length=20, default='')
    feedback_date = models.DateField(default=date.today)
    feedback_status = models.CharField(max_length=10, default='')

    def __str__(self):
        return self.feedback_desc

