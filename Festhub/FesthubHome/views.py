from django.shortcuts import render


def FesthubHome(request):

    return render(request, "Homepage/home.html")
