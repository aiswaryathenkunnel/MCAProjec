from django.shortcuts import render, redirect
from studreg.models import Studreg
from django.db import connection
from django.contrib import messages


def Studview(request):
    userobj = Studreg.objects.filter(stud_status='')

    return render(request, "viewstuddetails/viewstuddetails.html", {'data': userobj})


def verify_details(request, pk):
    cursor = connection.cursor()
    cursor.execute("update studreg_studreg set stud_status='verified' where id='%s'" % (pk,))
    messages.info(request, "Verified successfully")
    return redirect('viewstuddetails:viewstudurl')

def reject_details(request, pk):
    cursor = connection.cursor()
    cursor.execute("update studreg_studreg set stud_status='rejected' where id='%s' " % (pk,))
    messages.info(request, "Rejected your submission")
    return redirect('viewstuddetails:viewstudurl')