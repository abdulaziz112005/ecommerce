from django.contrib import admin
from .models import Staff

class StaffAdmin(admin.ModelAdmin):
    list_display = ['id', 'last_name', 'first_name', 'phone_number']

admin.site.register(Staff, StaffAdmin)