from django.contrib import admin

# Register your models here.
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'photo']

admin.site.register(Category, CategoryAdmin)

class BrendAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'logo']

admin.site.register(Brend, BrendAdmin)

class ModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(Model, ModelAdmin)