# Generated by Django 3.2.3 on 2024-07-11 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_rename_user_leaves_userx'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leaves',
            old_name='userx',
            new_name='user',
        ),
    ]
