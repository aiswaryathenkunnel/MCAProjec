from django.db import models


class Depttype(models.Model):
    name = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.name
