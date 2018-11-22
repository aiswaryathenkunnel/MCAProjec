from django.conf.urls import url
from .views import Complaintview, verify_details, reject_details


app_name = 'viewcomplaint'
urlpatterns=[
    url(r'^$', Complaintview, name='Compurl'),
    url(r'^verify_complaint/(?P<pk>\d+)/$', verify_details, name='verify_details'),
    url(r'^reject_complaint/(?P<pk>\d+)/$', reject_details, name='reject_details'),
]