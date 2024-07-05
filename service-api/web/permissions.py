from rest_framework import permissions
from web.models import *

class PermissionIsLogin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.META['IS_LOGIN']

class PermissionApprover(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.META['ROLE'] == 'supervisor'