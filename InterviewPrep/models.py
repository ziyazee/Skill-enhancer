from django.db import models

# Create your models here.


class InterviewExperience(models.Model):
    companyName=models.CharField(max_length=500)
    companyExperience=models.CharField(max_length=5000)

class Aptitude(models.Model):
    topicName=models.CharField(max_length=500)
    topicDescription=models.CharField(max_length=5000)

class popularCodingProblems(models.Model):
    topicHeading=models.CharField(max_length=500)
    topicDescription=models.CharField(max_length=5000)

class InterviewExperiences(models.Model):
    userName=models.CharField(max_length=500)

    companyName=models.CharField(max_length=500)
    companyExperience=models.CharField(max_length=5000)


class Aptitud(models.Model):
    userName=models.CharField(max_length=500)
    topicName=models.CharField(max_length=500)
    topicDescription=models.CharField(max_length=5000)

class popularCodingProblem(models.Model):
    userName=models.CharField(max_length=500)

    topicHeading=models.CharField(max_length=500)
    topicDescription=models.CharField(max_length=5000)

class Subject(models.Model):
    userName=models.CharField(max_length=500)
    subjectName=models.CharField(max_length=500)
    topicHeading=models.CharField(max_length=500)
    topicDescription=models.CharField(max_length=5000)