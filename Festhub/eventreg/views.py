from django.shortcuts import render, redirect
from .import forms
from .models import Eventreg


def Eventregister(request):
    login_id = request.session['logid']
    model_object = Eventreg.objects.filter(id=login_id)

    if request.method == 'POST':
        form = forms.EventregForm(request.POST, request.FILES)
        if form.is_valid():
            regobj = form.cleaned_data
            eventid = regobj['event_id']
            eventregno = regobj['event_reg_no']
            a = Eventreg(event_id=eventid,  event_reg_no=eventregno, id=login_id)
            a.save()
        return redirect('eventreg:EventregForm')
    else:
        form = forms.EventregForm
    return render(request, "eventreg/eventreg.html", {'form': form, 'data': model_object})


