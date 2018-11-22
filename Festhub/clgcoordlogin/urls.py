from django.conf.urls import url
from .views import login, userhome


app_name = 'clgcoordlogin'

urlpatterns = [
    url(r'^$', login, name='clgcoordloginForm'),
    url(r'^userhome', userhome, name='userhome')
]