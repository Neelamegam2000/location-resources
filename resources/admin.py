from django.contrib import admin  
from .models import resources 
from mapbox_location_field.admin import MapAdmin  
  
admin.site.register(resources, MapAdmin)  
# Register your models here.
