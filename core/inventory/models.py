from django.db import models
from django.urls import reverse

# Create your models here.

# getting user model object
# User = get_user_model()


class Post(models.Model):
    """
    this is a class to define posts for blog app
    """

    author = models.ForeignKey("accounts.Profile", on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=250)
    content = models.TextField()
    status = models.BooleanField()
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title
    


class Category(models.Model):
    """
    this is a class to define categories for blog table
    """

    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    


class Site(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    capacity = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)



class DataCenter(models.Model):
    name = models.CharField(max_length=255, unique=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    security_level = models.PositiveBigIntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
    


class Room(models.Model):
    name = models.CharField(max_length=255)
    data_center = models.ForeignKey(DataCenter, to_field="name",on_delete=models.CASCADE)
    


class Rack(models.Model):
    name = models.CharField(max_length=255)
    data_center = models.ForeignKey(DataCenter, to_field="name",on_delete=models.CASCADE)
    rack_number = models.PositiveBigIntegerField()
    rack_height = models.PositiveBigIntegerField(null=True, blank=True)
    rack_width = models.PositiveBigIntegerField(null=True, blank=True)
    rack_depth = models.PositiveBigIntegerField(null=True, blank=True)
    rack_capacity = models.PositiveBigIntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Rack {self.rack_number} ({self.data_center.name})"

    

class Device(models.Model):
    rack = models.ForeignKey("Rack", on_delete=models.CASCADE)
    server = models.CharField(max_length=255)
    pdu = models.CharField(max_length=255)
    network_switch = models.CharField(max_length=255)


    def __str__(self):
        return str(self.rack)
    


class Power(models.Model):
    site = models.ForeignKey("Site", on_delete=models.CASCADE)
    ats = models.CharField(max_length=255)
    ups = models.CharField(max_length=255)
     
    def __str__(self):
        return str(self.site)


class DieselGenerator(models.Model):
    power = models.ForeignKey("Power", on_delete=models.CASCADE)
    manufacturer = models.CharField(max_length=255)


    def __str__(self):
        return str(self.power)