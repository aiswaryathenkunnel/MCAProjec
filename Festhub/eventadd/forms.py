from django import forms
from . import models


class EventaddForm(forms.ModelForm):
    class Meta:
        model = models.Eventadd
        fields = ['fest_id', 'event_name', 'event_desc', 'event_fees', 'part_type', 'max_part', 'time_from', 'time_to', 'venue']

