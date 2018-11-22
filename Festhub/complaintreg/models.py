from django.db import models


class Complaintreg(models.Model):
    stud_id = models.BigIntegerField()
    comp_desc = models.CharField(max_length=30, default='')
    comp_date = models.CharField(max_length=30, default='')
    comp_status = models.CharField(max_length=30, default='')
    comp_reply = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.comp_desc
