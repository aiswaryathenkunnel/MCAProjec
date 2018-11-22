from django import forms
from . import models


class FeedbackForm(forms.ModelForm):
    feedback_desc = forms.CharField(
        required=True,
        label='description',
        max_length=30,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z]+', 'title': 'enter numeric character only'})
    )

    class Meta:
        model = models.Feedback
        fields = ['feedback_desc', 'feedback_date']