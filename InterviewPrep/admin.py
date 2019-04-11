from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Subjects)
class  kundan(admin.ModelAdmin):
    list_display=['subjectName','topicHeading','topicDescription']

@admin.register(InterviewExperience)
class  kundan(admin.ModelAdmin):
    list_display=['companyName','companyExperience']

@admin.register(Aptitude)
class  kundan(admin.ModelAdmin):
    list_display=['topicName','topicDescription']

@admin.register(popularCodingProblems)
class  kundan(admin.ModelAdmin):
    list_display=['topicHeading','topicDescription']
