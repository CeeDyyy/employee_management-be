from re import sub
from oauth2_provider.models import (
    AccessToken,
)
# from base.utils import get_client_ip
import jwt

class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        # request.META['IP'] = get_client_ip(request)

        header_token = request.META.get('HTTP_AUTHORIZATION', None)
        access_token = None
        if header_token is not None:
            access_token = sub('Token ', '', header_token)  #ตัดคำว่า Token ออก
            decoded_jwt = jwt.decode(access_token, "secret", algorithms=["HS256"])
            request.META['ROLE'] = decoded_jwt['role']
            request.META['IS_LOGIN'] = True
        else:
            request.META['IS_LOGIN'] = False
            
        response = self.get_response(request)
        return response