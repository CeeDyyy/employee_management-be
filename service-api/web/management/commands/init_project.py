from django.core.management.base import BaseCommand
from django.conf import settings
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.utils import IntegrityError
from web.models import *
from web.models.option import *
from django.core.management import call_command
from oauth2_provider.models import (
    Application, 
)
from django.contrib.auth import authenticate
from web.models.auth_token import AuthToken

class Command(BaseCommand):
    def handle(self, *args, **options):
        addPermission()
        addGroup()   
        call_command('loaddata','/usr/src/app/initdata/auth.json')
        # create_token_superuser()
        # addLang()
        

def addPermission():
    content_type = ContentType.objects.get(app_label='auth', model='group')
    perms = [
        # ('backoffice_manage','จัดกา'),
    ]
    for p in perms:
        try:
            Permission.objects.get(codename=p[0])
            Permission.objects.filter(codename=p[0]).update(name=p[1], content_type=content_type)
        except Permission.DoesNotExist:
            Permission.objects.create(codename=p[0], name=p[1], content_type=content_type)
        except Exception as e:
            print('addPermission: Exception =>',e)

def addGroup():
    groups = [
        {
            'name': 'STAFF',
            'perms': [
                # 'backoffice_manage_league',
                # 'backoffice_manage_match',
                # 'backoffice_manage_team',
                # 'backoffice_manage_channel',
            ]
        },
        {
            'name': 'ADMIN',
            'perms': [
                # 'backoffice_manage_user_auth',
                # 'backoffice_manage_partner',
                # 'backoffice_manage_league',
                # 'backoffice_manage_match',
                # 'backoffice_manage_team',
                # 'backoffice_manage_channel',
            ]
        },
    ]
    perms = Permission.objects.all()
    for g in groups:
        group, created = Group.objects.get_or_create(name=g['name'])
        perm_groups = perms.filter(codename__in=g['perms'])
        group.permissions.clear()
        group.permissions.set(perm_groups)

def create_token_superuser():
        try:
            application = Application.objects.get(name='SERVICE_API')
        except Application.DoesNotExist:
            application = Application.objects.create(name='SERVICE_API')
        user = authenticate(username='admin', password='admin')
        AuthToken.create_token(user,application)

# def addLang():
#     langs = [
#         {
#             'short_lang': 'th',
#             'lang': 'ภาษาไทย',
#         },
#         {
#             'short_lang': 'en',
#             'lang': 'English',
#         }
#     ]
#     for l in langs:
#         try:
#             NativeLanguage.objects.get(short_lang=l['short_lang'])
#         except NativeLanguage.DoesNotExist:
#             NativeLanguage.objects.create(short_lang=l['short_lang'],lang=l['lang'])