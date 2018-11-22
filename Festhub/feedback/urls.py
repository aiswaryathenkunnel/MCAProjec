from django.conf.urls import url
from .views import feedback

app_name = 'feedback'


urlpatterns = [
    url(r'^$', feedback, name='FeedbackForm')
]

