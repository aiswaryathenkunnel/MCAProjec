"""Festhub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^clgcoordreg/', include('collegecoordreg.urls')),
    url(r'^clgcoordlogin/', include('clgcoordlogin.urls')),
    url(r'^studreg/', include('studreg.urls')),
    url(r'^studlogin/', include('studlogin.urls')),
    url(r'^festadd/', include('festadd.urls')),
    url(r'^eventadd/', include('eventadd.urls')),
    url(r'^viewfest/', include('viewfestdetails.urls')),
    url(r'^viewevent/', include('vieweventdetails.urls')),
    url(r'^eventreg/', include('eventreg.urls')),
    url(r'^complaintreg/', include('complaintreg.urls')),
    url(r'^viewcoord/', include('viewcoorddetails.urls')),
    url(r'^viewstud/', include('viewstuddetails.urls')),
    url(r'^feedback/', include('feedback.urls')),
    url(r'^viewcomp/', include('viewcomplaint.urls')),
    url(r'^festhub/', include('FesthubHome.urls')),
    url(r'^Registration/', include('Registrationpage.urls')),
    url(r'^Login/', include('Loginhomepage.urls')),
    url(r'^viewfeedback/', include('viewfeedback.urls')),

]
