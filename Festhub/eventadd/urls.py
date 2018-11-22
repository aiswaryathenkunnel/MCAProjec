from django.conf.urls import url
from . views import Eventinsert


app_name = 'eventadd'
urlpatterns=[
    url(r'^$', Eventinsert, name='EventaddForm')
]