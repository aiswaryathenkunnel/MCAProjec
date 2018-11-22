from django.conf.urls import url
from . views import Collegecoordreg


app_name = 'collegecoordreg'
urlpatterns= [
    url(r'^$', Collegecoordreg, name='CollegecoordregForm')
]