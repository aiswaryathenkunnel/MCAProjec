from django import forms
from . import models


class EventregForm(forms.ModelForm):
    class Meta:
        model = models.Eventreg
        fields = ['event_id', 'event_reg_no']