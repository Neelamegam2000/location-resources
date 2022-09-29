from email.policy import default
from unicodedata import name
from django.db import models
from mapbox_location_field.models import LocationField,AddressAutoHiddenField 
class resources(models.Model): 
    name = models.CharField(max_length=100)
    location = LocationField(map_attrs = {  
 "style": "mapbox://styles/mapbox/streets-v11",
 "zoom": 30,
 "center": [22.1991660760527,78.476681027237],
 "cursor_style": 'pointer',
 "marker_color": "blue",
 "rotate": True,
 "geocoder": True,
 "fullscreen_button": True,
 "navigation_buttons": True,
 "track_location_button": True, 
 "readonly": True,
 "placeholder": "Pick a location on map below", 
 "language": "auto",
 "message_404": "undefined address", })
    address = AddressAutoHiddenField()
    pincode= models.CharField(max_length=50) 
    work=models.CharField(max_length=100) 
    email=models.EmailField() 
    phone_number=models.CharField(max_length=12) 
    review=models.CharField(max_length=500,blank=True)
    profile_picture=models.ImageField(upload_to='profile_picture/',blank=True,default='profile_picture/avatar.jpg')
    def __str__(self):
        return "%s %s %s %s" %(self.name,self.work,self.location,self.pincode)
class login(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField()
	password=models.CharField(max_length=16)
	def __str__(self):
		return "%s" %(self.name)

class status(models.Model):
    resources_id = models.ForeignKey(resources, on_delete=models.CASCADE)
    status = models.CharField(max_length=255,choices=(("Available","Available"),("On Duty","On Duty"),("Break","Break"),("Open","Open"),("closed","Closed")),default="Available");
    def __resources__(self):
        return self.resources_id 

