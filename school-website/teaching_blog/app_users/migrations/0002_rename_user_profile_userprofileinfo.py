# Generated by Django 3.2 on 2021-04-29 14:17

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user_profile',
            new_name='UserProfileInfo',
        ),
    ]
