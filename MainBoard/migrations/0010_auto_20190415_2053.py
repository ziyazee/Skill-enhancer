# Generated by Django 2.1.8 on 2019-04-15 15:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainBoard', '0009_auto_20190415_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]