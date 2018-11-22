from django import forms
from . import models


class CollegecoordregForm(forms.ModelForm):
    class Meta:
        model = models.Collegecoordreg
        fields = ['coord_name', 'coord_contactno', 'coord_email', 'clg_name', 'clg_website', 'clg_contactno', 'clg_place', 'clg_pincode', 'clg_dist', 'clg_startdate', 'clg_licenceno', 'clg_type', 'clg_username', 'clg_password']