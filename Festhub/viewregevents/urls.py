from django.conf.urls import url
from . views import Regview


app_name = 'viewregevents'
urlpatterns=[
    url(r'^$', Regview, name='Regurl'),
    #url(r'^edit_festdetails/(?P<pk>\d+)/$', Festedit, name='edit_festdetails'),
]