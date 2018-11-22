from django.conf.urls import url
from .views import RegistrationHome

app_name = 'Registrationpage'


urlpatterns = [
    url(r'^$', RegistrationHome, name='Reghomeurl')
]