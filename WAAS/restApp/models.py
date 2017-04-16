from django.db import models


class Location(models.Model):
    fileurl = models.CharField(max_length=2048)
    nickname = models.CharField(max_length=100)
    logicalgroup = models.CharField(max_length=100)
