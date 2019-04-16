# Generated by Django 2.1.8 on 2019-04-15 14:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MainBoard', '0002_auto_20190409_1128'),
    ]

    operations = [
        migrations.CreateModel(
            name='myProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usersScore', models.CharField(default=None, max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]