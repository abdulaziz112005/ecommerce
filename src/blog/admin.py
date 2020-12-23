from django.contrib import admin

from .models import *


class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'photo']

admin.site.register(Blog, BlogAdmin)