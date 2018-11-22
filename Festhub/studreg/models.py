from django.db import models
from collegecoordreg.models import Collegecoordreg
from depttype.models import Depttype


class Studreg(models.Model):
    stud_name = models.CharField(max_length=30, default='')
    stud_place = models.CharField(max_length=30, default='')
    stud_email = models.CharField(max_length=30, default='')
    stud_contactno = models.CharField(max_length=30, default='')
    stud_age = models.CharField(max_length=30, default='')
    clg_id = models.ForeignKey(Collegecoordreg, on_delete=models.CASCADE)
    dept_id = models.ForeignKey(Depttype, on_delete=models.CASCADE)
    stud_admno = models.CharField(max_length=30, default='')
    stud_course = models.CharField(max_length=30, default='')
    stud_batch = models.CharField(max_length=30, default='')
    stud_username = models.CharField(max_length=30, default='')
    stud_password = models.CharField(max_length=30, default='')
    stud_status = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.stud_name

