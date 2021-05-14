from django.db import models 
from mapbox_location_field.models import LocationField,AddressAutoHiddenField 
class resources(models.Model): 
    name = models.CharField(max_length=100)
    location = LocationField(map_attrs={"center": [0,0],"marker_color": "blue"})
    address = AddressAutoHiddenField()
    pincode= models.CharField(max_length=50) 
    work=models.CharField(max_length=100) 
    email=models.EmailField() 
    phone_number=models.CharField(max_length=12) 
    def __str__(self):
        return "%s %s %s %s" %(self.name,self.work,self.location,self.pincode)
