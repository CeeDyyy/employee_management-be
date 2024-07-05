from django.db import models
from web.models.option import *

class SystemSetting(models.Model):
    setting = models.CharField(max_length=20, choices=SETTING_KEY)
    value = models.TextField(default='')

    def __str__(self):
        return '%s' % (self.setting)
    
