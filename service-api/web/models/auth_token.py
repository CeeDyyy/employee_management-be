import datetime
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User, Group
from oauth2_provider.models import (
    AccessToken,
    RefreshToken,
)
from dateutil.relativedelta import relativedelta
from django.db.models.signals import m2m_changed

def signal_set_staff_user(sender,instance,action,pk_set, **kwarg):
    if action == 'post_add':
        if pk_set is not None:
            if list(pk_set):
                sender.objects.filter(user=instance).exclude(group=list(pk_set)[0]).delete()
    # if action in ['post_remove','post_add','post_clear']:
    #     instance.is_staff = 'backoffice_manage_user_auth' in instance.get_group_permissions()
    #     instance.save(update_fields=['is_staff'])

# def signal_permission_group(instance,action, **kwarg):
#     if action in ['post_remove','post_add','post_clear']:
#         is_staff = bool(instance.permissions.filter(codename='backoffice_manage_user_auth').first())
#         instance.user_set.all().update(is_staff=is_staff)

m2m_changed.connect(signal_set_staff_user, sender=User.groups.through)
# m2m_changed.connect(signal_permission_group, sender=Group.permissions.through)

class AuthToken:
    def create_token(user,application):

        date_1 = datetime.datetime.today()
        access_token = AccessToken.objects.create(
            user=user,
            application = application,
            expires = date_1 + relativedelta(years=100),
            token = get_random_string(length=30, allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'),
            scope = 'read write'
        )
        AccessToken.objects.filter(user=user).exclude(token=access_token.token).delete()

        r = RefreshToken.objects.create(
            access_token = access_token,
            application = application,
            token = get_random_string(length=30, allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'),
            user = user
        )
        RefreshToken.objects.filter(user=user).exclude(access_token=access_token).delete()

        return r