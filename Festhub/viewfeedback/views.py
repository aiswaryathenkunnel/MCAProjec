from django.shortcuts import render, redirect
from django.db import connection
from django.contrib import messages
from feedback.models import Feedback


def Feedbackview(request):
    userobj = Feedback.objects.filter(feedback_status='')

    return render(request, "viewfeedback/viewfeedback.html", {'data': userobj})


def verify_details(request, pk):
    cursor = connection.cursor()
    cursor.execute("update feedback_feedback set feedback_status='verified' where id='%s'" % (pk,))
    messages.info(request, "Verified successfully")
    return redirect('viewfeedback:feedbackurl')

def reject_details(request, pk):
    cursor = connection.cursor()
    cursor.execute("update feedback_feedback set feedback_status='Not verified' where id='%s' " % (pk,))
    messages.info(request, "Not verified your submission")
    return redirect('viewfeedback:feedbackurl')