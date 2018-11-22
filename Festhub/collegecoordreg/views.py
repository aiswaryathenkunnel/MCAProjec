from django.shortcuts import render, redirect
from .import forms
from django.core.mail import EmailMessage


def Collegecoordreg(request):
    if request.method == "POST":
        form = forms.CollegecoordregForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            obj = form.cleaned_data
            mail = obj['coord_email']
            username = obj['clg_username']
            password = obj['clg_password']
            instance.save()
            #coord_email = EmailMessage('Registration completed', 'Your registration process is successfully Completed with username: '+username+' and Password :'+password, to=[mail])
            #coord_email.send()
            msg = "Inserted successfully"
            return redirect('collegecoordreg:CollegecoordregForm')
    else:
        form = forms.CollegecoordregForm
        msg = "Not inserted"
    return render(request, "collegecoordreg/collegecoordreg.html", {'form': form, 'msg': msg})
