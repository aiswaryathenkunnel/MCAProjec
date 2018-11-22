from django.conf.urls import url
from . views import Festview


app_name = 'viewfestdetails'
urlpatterns=[
    url(r'^$', Festview, name='Festurl'),
    #url(r'^edit_festdetails/(?P<pk>\d+)/$', Festedit, name='edit_festdetails'),
]