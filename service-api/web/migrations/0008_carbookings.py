# Generated by Django 3.2.3 on 2024-03-25 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarBookings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(blank=True, max_length=64, null=True)),
                ('detail', models.CharField(blank=True, max_length=512, null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('car_id', models.CharField(blank=True, max_length=64, null=True)),
                ('record_timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(blank=True, max_length=8, null=True)),
                ('approver', models.CharField(blank=True, max_length=64, null=True)),
                ('reason', models.CharField(blank=True, max_length=512, null=True)),
                ('update_timestamp', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
