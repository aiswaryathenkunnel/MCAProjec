from django.shortcuts import render, redirect
from . import forms
from studreg.models import Studreg


def userhome(request):
    return render(request, 'studloginhome/studloginhome.html', {'logidd': request.session['logid']})


def login(request):
    if request.method == 'POST':
        form = forms.StudloginForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            password = userObj['password']

            if Studreg.objects.filter(stud_username=username).exists() and Studreg.objects.filter(stud_password=password).exists() and Studreg.objects.filter(stud_status="verified").exists():
                obj = Studreg.objects.get(stud_username=username)

                request.session['logid'] = obj.id
                return redirect('studlogin:userhome')

            else:
                return render(request, 'studlogin/studlogin.html', {'form': form})
    else:
        form = forms.StudloginForm()
    return render(request, 'studlogin/studlogin.html', {'form': form})