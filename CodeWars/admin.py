# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


from .models import CodingSets

@admin.register(CodingSets)
class  Ziya(admin.ModelAdmin):
    list_display=['Title','Description',]
