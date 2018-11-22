from django.conf.urls import url
from . views import Eventview


app_name = 'vieweventdetails'
urlpatterns=[
    url(r'^$', Eventview, name='Eventurl')
]