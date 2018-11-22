from django.shortcuts import render, redirect
from . import forms
from collegecoordreg.models import Collegecoordreg


def userhome(request):
    return render(request, 'clgcoordloginhome/clgcoordloginhome.html', {'logidd': request.session['logid']})


def login(request):
    if request.method == 'POST':
        form = forms.ClgcoordloginForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            password = userObj['password']

            if Collegecoordreg.objects.filter(clg_username=username).exists() and Collegecoordreg.objects.filter(clg_password=password).exists() and Collegecoordreg.objects.filter(clg_status="verified").exists():
                obj = Collegecoordreg.objects.get(clg_username=username)

                request.session['logid'] = obj.id
                return redirect('clgcoordlogin:userhome')

            else:
                return render(request, 'clgcoordlogin/clgcoordlogin.html', {'form': form})
    else:
        form = forms.ClgcoordloginForm()
    return render(request, 'clgcoordlogin/clgcoordlogin.html', {'form': form})