from django.contrib import admin

from .models import clasyear
from .models import filest

@admin.register(filest)
class  Ziya(admin.ModelAdmin):
    list_display=['fname','fdescription','usn','categorie',]


@admin.register(clasyear)
class  Ziya(admin.ModelAdmin):
    list_display=['choice','year','name','description',]

   
#admin.site.register(admin,Myinfo)