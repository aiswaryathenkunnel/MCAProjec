from django.conf.urls import url
from .views import Feedbackview, verify_details, reject_details


app_name = 'viewfeedback'
urlpatterns=[
    url(r'^$', Feedbackview, name='feedbackurl'),
    url(r'^verify_complaint/(?P<pk>\d+)/$', verify_details, name='verify_details'),
    url(r'^reject_complaint/(?P<pk>\d+)/$', reject_details, name='reject_details'),
]