import logging
import sys
from django.conf import settings

class Logging:

    def __init__(self,app_name):
        self.app_name = app_name
        self.getLogger()

    def getLogger(self):
        return logging.getLogger('mongolog')
    
    def log(self,level,data):
        data['app_name'] = self.app_name
        data['level'] = level
        if settings.IS_LOGGING:
            l = self.getLogger()

            if level == 'info':
                l.info(data)
            elif level == 'error':
                l.error(data)
            elif level == 'debug':
                l.debug(data)
            elif level == 'warning':
                l.warn(data)
        return data

    def info(self,action, user, data=None):
        return self.log('info',{
            'action': action,
            'user': user,
            'data': data
        })

    def error(self, action, user, data=None):
        return self.log('error',{
            'action': action,
            'user': user,
            'data': data
        })

    def debug(self, action, user, data=None):
        return self.log('debug',{
            'action': action,
            'user': user,
            'data': data
        })
    
    def warning(self,action, user, data=None):
        return self.log('warning',{
            'action': action,
            'user': user,
            'data': data
        })
    
    def debug(self,action, data=None):
        if settings.IS_LOGGING:
            print({
                'action': action,
                'data': data
            },file=sys.stderr)