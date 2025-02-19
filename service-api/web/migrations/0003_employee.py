# Generated by Django 3.2.3 on 2023-07-13 21:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0002_auto_20230215_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=20, unique=True)),
                ('status', models.IntegerField(choices=[(1, 'เปิดใช้งาน'), (0, 'ปิดใช้งาน')], default=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_employee', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
