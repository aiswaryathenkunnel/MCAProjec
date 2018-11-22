from django.shortcuts import render, redirect, get_object_or_404
from .import forms
from .models import Festadd

def Festinsert(request):
    login_id = request.session['logid']
    model_object = Festadd.objects.filter(clg_id=login_id)

    if request.method == 'POST':
        form = forms.FestaddForm(request.POST, request.FILES)
        if form.is_valid():
            festobj = form.cleaned_data
            name = festobj['fest_name']
            theme = festobj['fest_theme']
            deptid = festobj['dept_id']
            date = festobj['fest_date']
            type = festobj['fest_type']
            a = Festadd(fest_name=name, fest_theme=theme, clg_id=request.session['logid'], dept_id=deptid, fest_date=date, fest_type=type)
            a.save()
        return redirect('festadd:FestaddForm')
    else:
        form = forms.FestaddForm
    return render(request, "festadd/festadd.html", {'form': form, 'data': model_object})

def Festedit(request, pk):
    template = 'festadd/festadd.html'
    post = get_object_or_404(Festadd, pk=pk)
    model_object = Festadd.objects.all()
    if request.method == 'POST':
        form = forms.FestaddForm(request.POST, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('festadd:FestaddForm')
    else:
        form = forms.FestaddForm(instance=post)
        context = {
            'form': form,
            'post': post,
            'data': model_object,
        }
    return render(request, template, context)


def Festdelete(request, pk):
    post = get_object_or_404(Festadd, pk=pk)
    post.delete()
    return redirect('festadd:FestaddForm')
