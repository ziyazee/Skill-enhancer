# Generated by Django 2.1.8 on 2019-04-15 15:29

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MainBoard', '0010_auto_20190415_2053'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='myProfile',
            new_name='Profile',
        ),
    ]