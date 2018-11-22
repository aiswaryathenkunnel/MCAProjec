from django.conf.urls import url
from .views import Coordview, verify_details, reject_details


app_name = 'viewcoorddetails'
urlpatterns=[
    url(r'^$', Coordview, name='viewcoordurl'),
    url(r'^verify_coorddetails/(?P<pk>\d+)/$', verify_details, name='verify_details'),
    url(r'^reject_coorddetails/(?P<pk>\d+)/$', reject_details, name='reject_details'),
]