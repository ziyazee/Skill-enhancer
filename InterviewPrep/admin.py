from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Subject)
class  kundan(admin.ModelAdmin):
    list_display=['userName','subjectName','topicHeading','topicDescription']

@admin.register(InterviewExperiences)
class  kundan(admin.ModelAdmin):
    list_display=['userName','companyName','companyExperience']

@admin.register(Aptitud)
class  kundan(admin.ModelAdmin):
    list_display=['userName','topicName','topicDescription']

@admin.register(popularCodingProblem)
class  kundan(admin.ModelAdmin):
    list_display=['userName','topicHeading','topicDescription']
