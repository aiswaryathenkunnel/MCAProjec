from django.shortcuts import render, redirect
from . import forms
from .models import Feedback


def feedback(request):
    login_id = request.session['logid']
    model_object = Feedback.objects.filter(stud_id=login_id)
    if request.method == 'POST':
        form = forms.FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            FeeObj = form.cleaned_data
            description = FeeObj['feedback_desc']
            date = FeeObj['feedback_date']
            a = Feedback(stud_id=request.session['logid'], feedback_desc=description, feedback_date=date)
            a.save()
        return redirect('feedback:FeedbackForm')
    else:
        form = forms.FeedbackForm
    return render(request, "feedback/feedback.html", {'form': form, 'data': model_object})
