from django.db import models
from web.models.option import *

class Users(models.Model):
    user_id = models.CharField(max_length=64, null=True, blank=True, unique=True)
    display_name = models.CharField(max_length=64, null=True, blank=True)
    status_message = models.CharField(max_length=500, null=True, blank=True)
    picture_url = models.CharField(max_length=255, null=True, blank=True)
    name_en_first = models.CharField(max_length=64, null=True, blank=True)
    name_en_middle = models.CharField(max_length=64, null=True, blank=True)
    name_en_last = models.CharField(max_length=64, null=True, blank=True)
    name_en_nick = models.CharField(max_length=64, null=True, blank=True)
    name_local_first = models.CharField(max_length=64, null=True, blank=True)
    name_local_middle = models.CharField(max_length=64, null=True, blank=True)
    name_local_last = models.CharField(max_length=64, null=True, blank=True)
    name_local_nick = models.CharField(max_length=64, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    position = models.CharField(max_length=64, null=True, blank=True)
    section = models.CharField(max_length=64, null=True, blank=True)
    division = models.CharField(max_length=64, null=True, blank=True)
    department = models.CharField(max_length=64, null=True, blank=True)
    branch = models.CharField(max_length=64, null=True, blank=True)
    company = models.CharField(max_length=64, null=True, blank=True)
    rank = models.CharField(max_length=64, null=True, blank=True)
    role = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self):
        return '%s %s (%s)' % (
            self.name_local_first, self.name_local_last, self.name_local_nick
            )