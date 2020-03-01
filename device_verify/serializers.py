from .models import Device
from rest_framework import serializers

class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = ['name', 'mac_address', 'owner_name', 'router_name', 'online']
