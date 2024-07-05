from rest_framework import permissions
from django.shortcuts import get_object_or_404

# class IsAuthenticatedOrCreate(permissions.IsAuthenticated):
#     def has_permission(self, request, view):
#         if request.method == 'POST':
#             return True
#         return super(IsAuthenticatedOrCreate, self).has_permission(request, view)

# class IsAdminOnly(permissions.BasePermission):
    
#     def has_permission(self, request,view):
#         if request.method=='PATCH':
#             try:
#                 groups = request.user.groups.values_list('name', flat=True)
#                 group_list = list(groups)
#                 return 'admin' in group_list 
#             except :
#                 return False
#         else:
#             return True

# class IsPartnerOnly(permissions.BasePermission):
    
#     def has_permission(self, request,view):
#         if request.method=='PATCH' or request.method=='GET':
#             try:
#                 groups = request.user.groups.values_list('name', flat=True)
#                 group_list = list(groups)
#                 return 'partner' in group_list 
#             except :
#                 return False
#         else:
#             return True

# class IsPartnerOwnerOnly(permissions.BasePermission):
    
#     def has_permission(self, request,view):
#         if request.method=='PATCH':
#             partner = get_object_or_404(Partner, user__pk=request.user.pk)
#             pk = request.resolver_match.kwargs.get('pk')
#             get_device = DeviceTruemoney.objects.get(id=pk)
#             if get_device.partner.id == partner.id:
#                 return True
#             return False
#         else:
#             return True