# Generated by Django 3.2.3 on 2024-03-25 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_carbookings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carbookings',
            name='record_timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
