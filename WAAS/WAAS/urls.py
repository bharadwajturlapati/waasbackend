from django.conf.urls import url, include
from rest_framework import routers
from restApp import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'location', views.LocationViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^health-check/', include('health.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]