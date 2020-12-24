from django.contrib import admin
from .models import Delivery, Status

class DeliveryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'info', 'status']

class DeliveryStatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'info', 'status']

admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(Status, DeliveryStatusAdmin)