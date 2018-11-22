from django.shortcuts import render, redirect
from . import forms
from .models import Complaintreg


def complaintreg(request):
    login_id = request.session['logid']
    model_object = Complaintreg.objects.filter(stud_id=login_id)
    if request.method == 'POST':
        form = forms.ComplaintregForm(request.POST, request.FILES)
        if form.is_valid():
            ComObj = form.cleaned_data
            description = ComObj['comp_desc']
            complaintdate = ComObj['comp_date']
            a = Complaintreg(stud_id=request.session['logid'], comp_desc=description, comp_date=complaintdate)
            a.save()
        return redirect('complaintreg:ComplaintregForm')
    else:
        form = forms.ComplaintregForm
    return render(request, "complaintreg/complaintreg.html", {'form': form, 'data': model_object})

