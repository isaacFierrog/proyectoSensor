from django.contrib import admin
from .models import SensorModel


class SensorAdmin(admin.ModelAdmin):
    ordering = ['sensor_id']
    
    
admin.site.register(SensorModel, SensorAdmin)