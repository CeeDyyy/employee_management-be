# Generated by Django 3.2.3 on 2024-07-11 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_auto_20240711_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaves',
            name='user_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user_leave', to='web.users'),
        ),
    ]
