from django import forms
from . import models


class ComplaintregForm(forms.ModelForm):
    comp_desc = forms.CharField(
        required=True,
        label='description',
        max_length=30,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z]+', 'title': 'enter numeric character only'})
    )

    class Meta:
        model = models.Complaintreg
        fields = ['comp_desc', 'comp_date']