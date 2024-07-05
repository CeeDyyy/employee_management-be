import os
from django_b2.backblaze_b2 import BackBlazeB2
from django.conf import settings
from django.db import models
from django.dispatch import receiver

from django.utils.text import slugify


def signal_update_file(sender, instance, attr):
    if not hasattr(instance,'changed_fields'):
        instance.changed_fields = []

    try:
        old_file_obj = getattr(sender.objects.get(pk=instance.pk), attr)
    except sender.DoesNotExist:
        old_file_obj = None

    new_file_obj = getattr(instance, attr)
    if new_file_obj:
        if not old_file_obj == new_file_obj:
            instance.changed_fields.append(attr)

    if not old_file_obj:
        return False

    if old_file_obj == new_file_obj:
        return False
    if not os.path.isfile(old_file_obj.path):
        return False
    
    os.remove(old_file_obj.path)
    return True


def signal_delete_file(sender, instance, attr):
    file_obj = getattr(instance, attr, None)
    if not file_obj:
        return False
    if not os.path.isfile(file_obj.path):
        return False

    os.remove(file_obj.path)
    return True


def generate_slug(instance, fields, allow_unicode=True):
    for field in fields:
        value = getattr(instance, field, None)
        if value:
            return slugify(value, allow_unicode)
    return None

def signal_upload_file(instance):
    import sys
    if not hasattr(instance,'changed_fields'):
        instance.changed_fields = []
    # print(instance.changed_fields,file=sys.stderr)
    if not settings.USE_B2:
        return False
    if len(instance.changed_fields) == 0:
        return False
    b2 = BackBlazeB2()
    b2.authorize("production", settings.B2_KEY_ID, settings.B2_APP_KEY)
    b2.set_bucket(settings.B2_BUCKET_NAME)
    b2.set_bucket('ibizibzs-stg')
    
    for attr in instance.changed_fields:
        new_file_obj = getattr(instance, attr)
        if new_file_obj:
            src_path = new_file_obj.path
            # print(src_path,file=sys.stderr)
            if os.path.isfile(src_path):
                dest_path = '%s%s' % (settings.MEDIA_URL, str(new_file_obj))
                try:
                    b2.get_file_info_by_name(dest_path)
                except:
                    with open(src_path, 'rb') as f:
                        b2.upload_file(dest_path, f)
                        print('file:',dest_path,file=sys.stderr)
    instance.changed_fields.clear()
    return True

@receiver(models.signals.post_save)
def upload_post_save(sender, instance, **kwargs):
    return signal_upload_file(instance)
