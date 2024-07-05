# Generated by Django 3.2.3 on 2024-03-15 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_alter_cars_capacity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(blank=True, max_length=64, null=True, unique=True)),
                ('display_name', models.CharField(blank=True, max_length=64, null=True)),
                ('status_message', models.CharField(blank=True, max_length=500, null=True)),
                ('picture_url', models.CharField(blank=True, max_length=255, null=True)),
                ('name_en_first', models.CharField(blank=True, max_length=64, null=True)),
                ('name_en_middle', models.CharField(blank=True, max_length=64, null=True)),
                ('name_en_last', models.CharField(blank=True, max_length=64, null=True)),
                ('name_en_nick', models.CharField(blank=True, max_length=64, null=True)),
                ('name_local_first', models.CharField(blank=True, max_length=64, null=True)),
                ('name_local_middle', models.CharField(blank=True, max_length=64, null=True)),
                ('name_local_last', models.CharField(blank=True, max_length=64, null=True)),
                ('name_local_nick', models.CharField(blank=True, max_length=64, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('position', models.CharField(blank=True, max_length=64, null=True)),
                ('section', models.CharField(blank=True, max_length=64, null=True)),
                ('division', models.CharField(blank=True, max_length=64, null=True)),
                ('department', models.CharField(blank=True, max_length=64, null=True)),
                ('branch', models.CharField(blank=True, max_length=64, null=True)),
                ('company', models.CharField(blank=True, max_length=64, null=True)),
                ('rank', models.CharField(blank=True, max_length=64, null=True)),
                ('role', models.CharField(blank=True, max_length=64, null=True)),
            ],
        ),
    ]
