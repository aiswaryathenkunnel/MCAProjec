from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .import forms
from .models import Eventadd


def Eventinsert(request):
    loginid = request.session['logid']
    model_object = Eventadd.objects.filter(clg_id=loginid)
    if request.method == 'POST':
        form = forms.EventaddForm(request.POST, request.FILES)
        if form.is_valid():
            eventobj = form.cleaned_data
            festid = eventobj['fest_id']
            name = eventobj['event_name']
            desc = eventobj['event_desc']
            fees = eventobj['event_fees']
            parttype = eventobj['part_type']
            maxpart = eventobj['max_part']
            timefrom = eventobj['time_from']
            timeto = eventobj['time_to']
            venues = eventobj['venue']
            a = Eventadd(clg_id=request.session['logid'], fest_id=festid, event_name=name, event_desc=desc, event_fees=fees, part_type=parttype, max_part=maxpart, time_from=timefrom, time_to=timeto, venue=venues)
            a.save()
            messages.info(request, "insert")
        return redirect('eventadd:EventaddForm')
    else:
        form = forms.EventaddForm
    return render(request, "eventadd/eventadd.html", {'form': form, 'data': model_object})

def Eventedit(request, pk):
    template = 'eventadd/eventadd.html'
    post = get_object_or_404(Eventadd, pk=pk)
    model_object = Eventadd.objects.all()
    if request.method == 'POST':
        form = forms.FestaddForm(request.POST, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('eventadd:EventaddForm')
    else:
        form = forms.EventaddForm(instance=post)
        context = {
            'form': form,
            'post': post,
            'data': model_object,
        }
    return render(request, template, context)


def Eventdelete(request, pk):
    post = get_object_or_404(Eventadd, pk=pk)
    post.delete()
    return redirect('eventadd:EventaddForm')
