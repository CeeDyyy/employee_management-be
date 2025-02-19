from django.db import models
from web.models.option import *

class Cars(models.Model):
    title = models.CharField(max_length=64, null=True, blank=True)
    type = models.CharField(max_length=64, null=True, blank=True)
    capacity = models.IntegerField(null=True, blank=True)   #'max_length' is ignored when used with IntegerField
    license = models.CharField(max_length=64, null=True, blank=True,unique=True)

    def __str__(self):
        return '%s (%s)' % (self.title, self.license)