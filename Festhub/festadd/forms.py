from django import forms
from . import models


class FestaddForm(forms.ModelForm):
    class Meta:
        model = models.Festadd
        fields = ['fest_name', 'fest_theme', 'dept_id', 'fest_date', 'fest_type']