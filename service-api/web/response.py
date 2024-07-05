from rest_framework.response import Response as _Response
from rest_framework import status as _status
from django.utils.translation import gettext_lazy as _

def Response(data, status=None, message=None, template_name=None, headers=None, content_type=None):

    _data = {
        'data': data
    }

    if message is not None :
        _data['message'] = message
    else:
        _data['message'] = _('Success')

    if status is not None:
        _data['status'] = status
    else:
        _data['status'] = _status.HTTP_200_OK

    return _Response(_data, status,template_name,headers,content_type)