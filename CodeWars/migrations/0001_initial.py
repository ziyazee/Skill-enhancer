# Generated by Django 2.1.5 on 2019-02-26 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CodingSets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=500, unique=True)),
                ('Description', models.CharField(max_length=50000, unique=True)),
            ],
        ),
    ]
