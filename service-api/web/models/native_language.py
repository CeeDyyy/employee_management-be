from django.db import models
from web.models.option import *

class NativeLanguage(models.Model):
    short_lang = models.CharField(max_length=2,unique=True)
    lang = models.CharField(max_length=50)

    def __str__(self):
        return '%s (%s)' % (self.short_lang,self.lang)