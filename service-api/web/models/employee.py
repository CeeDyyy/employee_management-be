from django.db import models
from web.models.option import *
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, related_name='user_employee', on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20,unique=True)
    status = models.IntegerField(default=ENABLED,choices=IS_ENABLED)

    def __str__(self):
        return '%s' % (self.user.username)