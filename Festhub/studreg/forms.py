from django import forms
from . import models


class StudregForm(forms.ModelForm):
    class Meta:
        model = models.Studreg
        fields = ['stud_name', 'stud_place', 'stud_email', 'stud_contactno', 'stud_age', 'clg_id', 'dept_id', 'stud_admno', 'stud_course', 'stud_batch', 'stud_username', 'stud_password']
