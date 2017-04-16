from django.conf.urls import url, include
from restApp import urls as resturls

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(resturls)),
    url(r'^health-check/', include('health.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]