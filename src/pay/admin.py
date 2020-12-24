from django.contrib import admin
from .models import Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'info']

admin.site.register(Payment, PaymentAdmin)