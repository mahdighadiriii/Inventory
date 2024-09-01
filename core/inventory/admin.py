from django.contrib import admin
from .models import Site, DataCenter, Rack, Device, Power, DieselGenerator, Room

# Register your models here.



class SiteAdmin(admin.ModelAdmin):

    list_display = [
        "name",
        "location",
        "capacity",
    ]


class DataCenterAdmin(admin.ModelAdmin):
    
    list_display = [
        "name",
        "site",
        "security_level",
    ]


class RoomAdmin(admin.ModelAdmin):

    list_display = [

        "name",
        "data_center",
        
    ]


class RackAdmin(admin.ModelAdmin):

    list_display = [
        "name",
        "data_center",
        "rack_number",
        "rack_height",
        "rack_width",
        "rack_depth",
        "rack_capacity",

    ]

class DeviceAdmin(admin.ModelAdmin):

    list_display = [
        "rack",
        "server",
        "pdu",
        "network_switch",

    ]


admin.site.register(Site,SiteAdmin)
admin.site.register(DataCenter,DataCenterAdmin)

admin.site.register(Rack,RackAdmin)
admin.site.register(Device,DeviceAdmin)

admin.site.register(Room,RoomAdmin)

