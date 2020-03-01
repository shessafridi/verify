from django.db import models

class Device(models.Model):
    name = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=255)
    mac_address = models.CharField(max_length=255)
    router_name = models.CharField(max_length=255)
    online = models.BooleanField(default=True)
    objects = models.Manager() 

    def __str__(self):
        return self.name