from django.contrib import admin
from .models import Profile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.
@admin.register(Profile)
class  kundan(admin.ModelAdmin):
    list_display=['user','usersScore',]
