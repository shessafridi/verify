from django.shortcuts import render
from .models import Device
from rest_framework import viewsets
from .serializers import DeviceSerializer



class DeviceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


def index(request):
    count = Device.objects.count()
    onlineDevices = Device.objects.filter(online=True).count()
    devices = Device.objects.all()
    query = request.GET.get('mac')
    if query:
        devices = devices.filter(mac_address__icontains=query)
    context = {
        'devices': devices,
        'count':count,
        'online':onlineDevices,
        "home_page": "active"
    }
    return render(request,'device_verify/index.html',context)

def offline(request):
    count = Device.objects.count()
    onlineDevices = Device.objects.filter(online=True).count()
    devices = Device.objects.filter(online=False)
    query = request.GET.get('mac')
    if query:
        devices = devices.filter(mac_address__icontains=query,online=False)
    context = {
        'devices': devices,
        'count':count,
        'online':onlineDevices,
        'offline_page': 'active'
    }
    return render(request,'device_verify/index.html',context)