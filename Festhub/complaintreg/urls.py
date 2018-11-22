from django.conf.urls import url
from .views import complaintreg

app_name = 'complaintreg'


urlpatterns = [
    url(r'^$', complaintreg, name='ComplaintregForm')
]