__author__ = 'KH2034'
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.healthstatus, name='healthstatus'),
]