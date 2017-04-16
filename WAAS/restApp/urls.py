__author__ = 'KH2034'
from rest_framework import routers
from django.conf.urls import url, include
from restApp import views
from django.conf.urls import url

router = routers.DefaultRouter()
router.register(r'api/users', views.UserViewSet)
router.register(r'api/groups', views.GroupViewSet)
router.register(r'api/quickaccess', views.LocationViewSet)

urlpatterns = [
 url(r'^', include(router.urls)),
]