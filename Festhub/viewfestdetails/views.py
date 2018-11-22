from django.shortcuts import render, redirect
from . import forms
from festadd.models import Festadd


def Festview(request):
    #login_id = request.session['logid']
    #model_object = Festadd.objects.get(fest_id=login_id)
    model_object = Festadd.objects.all()

    return render(request, "viewfestdetails/viewfestdetails.html", {'data': model_object})
