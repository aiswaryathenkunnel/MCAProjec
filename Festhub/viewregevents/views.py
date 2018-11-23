from django.shortcuts import render, redirect
from eventreg.models import Eventreg


def Regview(request):

    model_object = Eventreg.objects.all()

    return render(request, "vieweventreg/vieweventreg.html", {'data': model_object})