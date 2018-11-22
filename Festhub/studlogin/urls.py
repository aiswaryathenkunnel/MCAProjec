from django.conf.urls import url
from .views import login, userhome


app_name = 'studlogin'

urlpatterns = [
    url(r'^$', login, name='studloginForm'),
    url(r'^userhome', userhome, name='userhome')
]
