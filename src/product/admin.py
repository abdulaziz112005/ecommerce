from django.contrib import admin

from .models import *
# Register your models here.

class AttributesAdmin(admin.ModelAdmin):
	list_display = ['id', 'name']

admin.site.register(Attributes, AttributesAdmin)

class ValuesAdmin(admin.ModelAdmin):
	list_display = ['id', 'name']

admin.site.register(Values, ValuesAdmin)

class ItemValueAdmin(admin.ModelAdmin):
	list_display = ['id', 'item_id','value_id']

admin.site.register(ItemValue, ItemValueAdmin)

class ItemsAdmin(admin.ModelAdmin):
	list_display = ['id', 'price','sale_percent','cnt']

admin.site.register(Items, ItemsAdmin)

class PhotoAdmin(admin.ModelAdmin):
	list_display = ['id', 'photo']

admin.site.register(Photo, PhotoAdmin)

class ProductAdmin(admin.ModelAdmin):
	list_display = ['id', 'name']

admin.site.register(Product, ProductAdmin)