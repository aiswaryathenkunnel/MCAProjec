from django import forms
from studreg.models import Studreg


class StudloginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label='Username',
        max_length=30
    )

    password = forms.CharField(
        required=True,
        label='Password',
        max_length=30,
        widget=forms.PasswordInput()
    )

    class Meta:
        model = Studreg
