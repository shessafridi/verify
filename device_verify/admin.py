from django.contrib import admin
from .models import Device


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'router_name', 'mac_address', 'owner_name')

admin.site.register(Device, DeviceAdmin)
