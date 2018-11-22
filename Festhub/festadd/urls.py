from django.conf.urls import url
from . views import Festinsert, Festedit, Festdelete


app_name = 'festadd'
urlpatterns=[
    url(r'^$', Festinsert, name='FestaddForm'),
    url(r'^edit_festdetails/(?P<pk>\d+)/$', Festedit, name='edit_festdetails'),
    url(r'^delete_festdetails/(?P<pk>\d+)/$', Festdelete, name='delete_festdetails'),
]

