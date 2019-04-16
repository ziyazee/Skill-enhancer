# Generated by Django 2.1.8 on 2019-04-15 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InterviewPrep', '0004_auto_20190415_1323'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aptitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=500)),
                ('topicName', models.CharField(max_length=500)),
                ('topicDescription', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='InterviewExperiences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=500)),
                ('companyName', models.CharField(max_length=500)),
                ('companyExperience', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='popularCodingProblem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=500)),
                ('topicHeading', models.CharField(max_length=500)),
                ('topicDescription', models.CharField(max_length=5000)),
            ],
        ),
    ]