from django.conf.urls import url
from . views import Studreg


app_name = 'studreg'
urlpatterns= [
    url(r'^$', Studreg, name='StudregForm')
]
