from django.conf.urls import url
from . views import Eventregister


app_name = 'eventreg'
urlpatterns=[
    url(r'^$', Eventregister, name='EventregForm')
]