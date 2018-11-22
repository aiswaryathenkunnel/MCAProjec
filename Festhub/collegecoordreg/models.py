from django.db import models
from datetime import date


class Collegecoordreg(models.Model):
    coord_name = models.CharField(max_length=30, default='')
    coord_contactno = models.CharField(max_length=15, default='')
    coord_email = models.CharField(max_length=30, default='')
    clg_name = models.CharField(max_length=30, default='')
    clg_website = models.CharField(max_length=30, default='')
    clg_contactno = models.CharField(max_length=30, default='')
    clg_place = models.CharField(max_length=30, default='')
    clg_pincode = models.CharField(max_length=30, default='')
    clg_dist = models.CharField(max_length=30, default='')
    clg_startdate = models.DateField(default=date.today)
    clg_licenceno = models.CharField(max_length=30, default='')
    clg_type = models.CharField(max_length=30, default='')
    clg_username = models.CharField(max_length=30, default='')
    clg_password = models.CharField(max_length=30, default='')
    clg_status = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.clg_name
