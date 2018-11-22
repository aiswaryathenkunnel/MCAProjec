from django.shortcuts import render, redirect
from .import forms
from django.core.mail import EmailMessage


def Studreg(request):
    if request.method == "POST":
        form = forms.StudregForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            obj = form.cleaned_data
            #mail = obj['stud_email']
            #username = obj['stud_username']
            #password = obj['stud_password']
            instance.save()
            #stud_email = EmailMessage('Registration completed','Your registration process is successfully Completed with username: ' + username + ' and Password :' + password,to=[mail])
            #stud_email.send()
            instance.save()
            return redirect('studreg:StudregForm')
    else:
        form = forms.StudregForm
    return render(request, "studreg/studreg.html", {'form': form})
