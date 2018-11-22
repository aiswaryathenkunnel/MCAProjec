from django.shortcuts import render, redirect
from complaintreg.models import Complaintreg
from django.db import connection
from django.contrib import messages


def Complaintview(request):
    userobj = Complaintreg.objects.filter(comp_status='')

    return render(request, "viewcomplaint/viewcomplaint.html", {'data': userobj})


def verify_details(request, pk):
    cursor = connection.cursor()
    cursor.execute("update complaintreg_complaintreg set comp_status='verified' where id='%s'" % (pk,))
    messages.info(request, "Verified successfully")
    return redirect('viewcomplaint:Compurl')

def reject_details(request, pk):
    cursor = connection.cursor()
    cursor.execute("update complaintreg_complaintreg set comp_status='Not verified' where id='%s' " % (pk,))
    messages.info(request, "Not verified your submission")
    return redirect('viewcoorddetails:Compurl')