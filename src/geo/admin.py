from django.contrib import admin

# Register your models here.
from .models import Regions, Districts


class RegionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


class DistrictAdmin(admin.ModelAdmin):
    list_display = ['id', 'region_title', 'title']

    def region_title(self, obj):
        return obj.region.title

admin.site.register(Regions, RegionAdmin)
admin.site.register(Districts, DistrictAdmin)