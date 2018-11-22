from django.conf.urls import url
from .views import FesthubHome

app_name = 'FesthubHome'


urlpatterns = [
    url(r'^$', FesthubHome, name='Homeurl')
]