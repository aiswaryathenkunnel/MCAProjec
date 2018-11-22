from django.shortcuts import render


def LoginHome(request):

    return render(request, "loginhome/loginhome.html")
