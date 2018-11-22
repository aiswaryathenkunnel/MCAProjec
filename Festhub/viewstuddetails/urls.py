from django.conf.urls import url
from .views import Studview, verify_details, reject_details


app_name = 'viewstuddetails'
urlpatterns=[
    url(r'^$', Studview, name='viewstudurl'),
    url(r'^verify_studdetails/(?P<pk>\d+)/$', verify_details, name='verify_details'),
    url(r'^reject_studdetails/(?P<pk>\d+)/$', reject_details, name='reject_details'),
]