from django.shortcuts import render, redirect
from collegecoordreg.models import Collegecoordreg
from django.db import connection
from django.contrib import messages


def Coordview(request):
    userobj = Collegecoordreg.objects.filter(clg_status='')

    return render(request, "viewcoorddetails/viewcoorddetails.html", {'data': userobj})


def verify_details(request, pk):
    cursor = connection.cursor()
    cursor.execute("update collegecoordreg_collegecoordreg set clg_status='verified' where id='%s'" % (pk,))
    messages.info(request, "Verified successfully")
    return redirect('viewcoorddetails:viewcoordurl')

def reject_details(request, pk):
    cursor = connection.cursor()
    cursor.execute("update collegecoordreg_collegecoordreg set clg_status='rejected' where id='%s' " % (pk,))
    messages.info(request, "Rejected your submission")
    return redirect('viewcoorddetails:viewcoordurl')