from django.conf.urls import url
from .views import LoginHome

app_name = 'Loginhomepage'


urlpatterns = [
    url(r'^$', LoginHome, name='Loginhomeurl')
]