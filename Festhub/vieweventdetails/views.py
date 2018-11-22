from django.shortcuts import render
from festadd.models import Festadd
from eventadd.models import Eventadd

def Eventview(request):
    #login_id = request.session['logid']
    #model_object = Festadd.objects.get(id=login_id)
    #model_object1 = Eventadd.objects.filter(id=model_object.id)
    #return render(request, "vieweventdetails/vieweventdetails.html", {'data':model_object, 'data1':model_object1})
    model_object = Eventadd.objects.all()

    return render(request, 'vieweventdetails/vieweventdetails.html', {'data': model_object})