from django.contrib.auth.models import User, Group
from restApp.models import Location
from restApp.serializers import LocationSerializer
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset =  Location.objects.all()
    serializer_class = LocationSerializer